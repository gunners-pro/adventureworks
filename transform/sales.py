import pandas as pd

class TransformSales:
    @staticmethod
    def expand_date(df: pd.DataFrame, column: str) -> pd.DataFrame:
        new_df = df.copy()
        new_df["year"] = new_df[column].dt.year
        new_df["month"] = new_df[column].dt.month
        new_df["day"] = new_df[column].dt.day
        return new_df