from utils.db_connection import get_database_connection
from extract.sales import extract_sales
from clean.sales import clean_sales
from transform.sales import TransformSales

if __name__ == "__main__":
    engine = get_database_connection()
    
    sales = extract_sales(engine)

    df_sales_clean = clean_sales(sales)

    df_transformed = TransformSales.add_column_month(df_sales_clean)

    print(df_transformed)
