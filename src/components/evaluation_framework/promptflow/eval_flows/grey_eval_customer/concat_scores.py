from promptflow import tool

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def concat_scores(fluency: str, realness: str) -> dict:

    output_json = {
                   'gpt_realness': realness,
                   'gpt_fluency': fluency
                   }
    
    return output_json
