"""
-Installed Cloudera ODBC Driver for apache hive
-Added DSN with configuration settings

"""
import pyodbc
import logging
import pandas as pd
import os
from dotenv import load_dotenv
"""pip install python-dotenv"""
load_dotenv("data/getdetails.env")
"""
host_name = os.getenv("HOST_NAME")
port = os.getenv("PORT")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")
"""
conn = pyodbc.connect("DSN=clouderahive513",autocommit=True)
print(conn)
curr = conn.cursor()
curr.execute("use hiveassignment")

#curr.execute("show tables")
for row in curr.tables():
    print("Table name: ",row.table_name," ,Database: ",row.table_schem," ,type: ",row.table_type)

print("*"*100)
print("Yearpart table column names: ")
for row in curr.columns(table='yearpart'):
    print("Column: ",row.column_name," , Data type: ",row.type_name,", Nullable: ",row.is_nullable)
print("*"*100)

curr.execute("select * from yearpart limit 10;")
ls = curr.fetchall()
for l in ls:
    print(l)
#df = pd.read_sql("select * from tempo",conn)
#print(df.head(10))
