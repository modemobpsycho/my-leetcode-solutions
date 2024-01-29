from typing import List
import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    column_names: list[str] = ["student_id", "age"]
    result = pd.DataFrame(student_data, columns=column_names)
    return result
