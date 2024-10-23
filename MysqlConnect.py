from pymysql import connect
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('mysql+pymysql://root:Cuppuchinno!1@localhost:3306/employees')
connection = engine.connect()
query='select * from departments'
df = pd.read_sql(query,connection)
print(df.head())
connection.close()