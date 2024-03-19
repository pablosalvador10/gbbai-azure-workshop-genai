from promptflow import tool

def parse_cosine_sime(cosine_sim: float) -> int:
    if cosine_sim >= .6:
        return 5
    elif cosine_sim >= 0.2:
        return 4
    elif cosine_sim >= -0.2:
        return 3
    elif cosine_sim >= -0.6:
        return 2
    else:
        return 1

@tool
def check_grade(cosine_sim: float, evaluation_score: int) -> bool:
    cosine_score = parse_cosine_sime(cosine_sim)
    return cosine_score == evaluation_score