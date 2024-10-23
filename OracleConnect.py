from jsonschema.benchmarks.contains import schema
from sqlalchemy import create_engine
import cx_Oracle
import pandas as pd
 # Create the engine using Oracle connection string

engine = create_engine('oracle+cx_oracle://system:Cuppuchinno@localhost:1521/xe',echo='debug')
 # Establish the connection


connection = engine.connect()
# Define your query
query = "SELECT * from jobs"
 # Execute the query and fetch the data into a pandas DataFrame
df = pd.read_sql(query, connection)
print(df.head())
 # Don't forget to close the connection when you're done
connection.close()