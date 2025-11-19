import pandas as pd
from pathlib import Path

def extract_sales(engine):
    query = \
        """
        SELECT
            soh.SalesOrderID,
            soh.OrderDate,
            soh.CustomerID,
            sod.ProductID,
            p.Name AS ProductName,
            sod.OrderQty,
            sod.UnitPrice,
            sod.LineTotal,
            soh.TotalDue,
            soh.SalesPersonID
        FROM Sales.SalesOrderHeader AS soh
        JOIN Sales.SalesOrderDetail AS sod
            ON soh.SalesOrderID = sod.SalesOrderID
        JOIN Production.Product AS p
            ON sod.ProductID = p.ProductID; 
        """
    
    current_dir = Path(__file__).parent
    parent_dir = current_dir.parent
    data = parent_dir / "data"
    data.mkdir(parents=True, exist_ok=True)

    df = pd.read_sql(query, engine)
    df.to_csv(data / 'sales.csv', index=False)

    return df
