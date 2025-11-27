import pandas as pd

class TransformSales:
    @staticmethod
    def add_column_month(df: pd.DataFrame) -> pd.DataFrame:
        df["month"] = df["OrderDate"].dt.month
        return df