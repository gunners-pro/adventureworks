from utils.db_connection import get_database_connection
from extract.sales import extract_sales

engine = get_database_connection()

print(extract_sales(engine))