import pandas as pd

def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df = df.drop_duplicates()
    df['SalesPersonID'] = df['SalesPersonID'].astype(int)
    df = df.round({"UnitPrice": 2, "LineTotal": 2, "TotalDue": 2})
    return df