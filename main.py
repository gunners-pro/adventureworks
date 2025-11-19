from utils.db_connection import get_database_connection
from extract.sales import extract_sales
from clean.sales import clean_sales

if __name__ == "__main__":
    engine = get_database_connection()
    
    sales = extract_sales(engine)

    sales_transformed = clean_sales(sales)

    print(sales_transformed.dtypes)
