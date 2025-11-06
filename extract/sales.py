import pandas as pd

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

    return pd.read_sql(query, engine)
