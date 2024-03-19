from promptflow import tool
from bs4 import BeautifulSoup


@tool
def html_check(html_string: str) -> bool:
    return bool(BeautifulSoup(html_string, "html.parser").find())