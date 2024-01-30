import pandas as pd


def pivotTable(weather: df.DataFrame) -> pd.DataFrame:
    return df.pivot(index="month", columns="city", values="temperature")
