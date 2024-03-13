from promptflow import tool

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def concat_scores(html_format: str, grade_accuracy: str) -> dict:

    output_json = {
                   'html_format': html_format,
                   'grade_accuracy': grade_accuracy
                   }
    
    return output_json
