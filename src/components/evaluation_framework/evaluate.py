from promptflow import PFClient
from promptflow.entities import AzureOpenAIConnection
from glob import glob
import argparse
import pandas as pd
import mlflow
import os


# Helper function to parse anda aggregate PromptFlow outputs
def parse_pf_runs(pf, pf_run, metric_list):
    details = pf.get_details(pf_run)
    results = {}

    for metric in metric_list:
        details[metric] = details['outputs.output'].apply(lambda x: x.get(metric))
        metric_df = details.loc[:, [metric]]
        metric_df[metric] = metric_df[metric].astype(int)
        results[metric] = metric_df[metric].mean()
    return results

# Helper funciton to merge dicitonaries
def merge_dicts(*dict_args):
    """
    Given any number of dictionaries, shallow copy and merge into a new dict,
    precedence goes to key-value pairs in latter dictionaries.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

# Helper funciton to setup aoai-connection
def init_aoai_connection(pf, api_key, api_base):
    # Initialize an AzureOpenAIConnection object
    connection = AzureOpenAIConnection(
        name="aoai-connection", 
        api_key=api_key, 
        api_base=api_base,
        api_version="2023-03-15-preview"
    )

    # Create the connection, note that api_key will be scrubbed in the returned result
    result = pf.connections.create_or_update(connection)
    return


# Driver funciton - execute flows
def execute_flows(grey_customer_data_path, grey_grader_data_path, red_test_data_path, api_key, api_base):

    # print(f"The STARTING working directory is: {os.getcwd()}")

    result = [os.path.join(dp, f) for dp, dn, filenames in os.walk('.') for f in filenames]
   #  print(result)

    pf = PFClient()
    init_aoai_connection(pf, api_key, api_base)

    # print(f"The BEFORE PATH ASSIGNMENT working directory is: {os.getcwd()}")

    # Define Flows and Data
    grey_customer_flow = "promptflow/eval_flows/grey_eval_customer"
    grey_grader_flow = "promptflow/eval_flows/grey_eval_grader" 
    red_eval_flow = "promptflow/eval_flows/red_eval"

    # Define env variables
    environment_variables = {"PF_WORKER_COUNT": "1"}

    # print(f"The BEFORE RUN working directory is: {os.getcwd()}")

    grey_customer = pf.run(
        flow=grey_customer_flow,
        data=grey_customer_data_path,
        environment_variables=environment_variables,
        column_mapping={  # map the url field from the data to the url input of the flow
        "generated_question": "${data.generated_question}"
        }
    )

    grey_cust_results = parse_pf_runs(pf, grey_customer, ["gpt_fluency", "gpt_realness"])

    # Run evaluation flows  to evaluate chat results
    grey_grader = pf.run(
        flow=grey_grader_flow,
        data=grey_grader_data_path,
        environment_variables=environment_variables,
        column_mapping={  # map the url field from the data to the url input of the flow
        "generated_question": "${data.generated_question}",
        "gt_response": "${data.ground_truth_response}",
        "user_response": "${data.user_response}",
        "evaluation": "${data.evaluation}",
        "evaluation_score": "${data.evaluation_score}"
        }
    )

    grey_grader_results = parse_pf_runs(pf, grey_grader, ['html_format', 'grade_accuracy'] )
    
    # Run evaluation flows  to evaluate chat results
    red_tests = pf.run(
        flow=red_eval_flow,
        data=red_test_data_path,
        environment_variables=environment_variables,
        column_mapping={  # map the url field from the data to the url input of the flow
        "user_input": "${data.user_response}",
        "chat_response": "${data.chat_response}"
        }
    )

    red_test_results = parse_pf_runs(pf, red_tests, ["red_test_pass"])

    results = merge_dicts(grey_cust_results, grey_grader_results, red_test_results)
    print(results)

    mlflow.start_run()
    for metric in results:
        mlflow.log_metric(metric, results[metric])
    mlflow.end_run()

    return results

parser = argparse.ArgumentParser()
parser.add_argument("--grey_customer_data", type=str)
parser.add_argument("--grey_grader_data", type=str)
parser.add_argument("--red_test_data", type=str)
parser.add_argument("--api_key", type=str)
parser.add_argument("--api_base", type=str)

args, _ = parser.parse_known_args()
'''
execute_flows(
    grey_customer_data_path=args.grey_customer_data,
    grey_grader_data_path=args.grey_grader_data,
    red_test_data_path=args.red_test_data,
    api_key=args.api_key,
    api_base=args.api_base
)'''

if __name__ == "__main__":

    execute_flows(
        grey_customer_data_path="../../../sample_data/sample_chat_outputs/grey_tests_customer.json",
        grey_grader_data_path="../../../sample_data/sample_chat_outputs/grey_tests_grader.json",
        red_test_data_path="../../../sample_data/sample_chat_outputs/red_tests.json",
        api_key= os.getenv('AZURE_OPENAI_KEY'),
        api_base= os.getenv('AZURE_OPENAI_ENDPOINT')
    )