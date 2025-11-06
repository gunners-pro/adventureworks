import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from sqlalchemy import create_engine, Engine

load_dotenv()

def get_database_connection() -> Engine:
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = quote_plus(os.getenv("DB_PASSWORD", ""))

    connection_string = (
        f"mssql+pyodbc://{user}:{password}@{host},{port}/{database}"
        "?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
    )

    return create_engine(connection_string)
