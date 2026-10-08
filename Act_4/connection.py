import pyodbc
import json
import pandas as pd


def get_data():

    with open("my_passwd.json", "r") as f:
        password = json.load(f)["my_password"]

    server = "clase3server.database.windows.net"
    database = "sql_act"
    username = "Gael"

    conn_str = (
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=no;"
    )

    conn = pyodbc.connect(conn_str)

    query = "SELECT * FROM SalesLT.SalesOrderDetail"

    datos = pd.read_sql(query, conn)

    conn.close()

    return datos