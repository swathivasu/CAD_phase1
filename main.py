import pandas as pd
from sqlalchemy import create_engine

# Connection details
host = 'localhost'
user = 'root'
password = '0412'
database = 'college'

# Create an SQLAlchemy engine
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

# Replace 'Data_Set.xlsx' with the path to your Excel file
excel_file = 'Data_Set.xlsx'

# Read Excel file into a Pandas DataFrame
df = pd.read_excel(excel_file)

# ETL Processes
# Data Cleaning
# Convert 'License Date' to datetime
df['License Date'] = pd.to_datetime(df['License Date'], format='%d-%b-%y')

# Data Transformation
# Convert 'License Status' to 1 for 'Yes' and 0 for 'No'
df['License Status'] = df['License Status'].map({'Yes': 1, 'No': 0})

# Convert letters in 'Boat Name' and 'Boat Type' to uppercase
df['Boat Name'] = df['Boat Name'].str.upper()
df['Boat Type'] = df['Boat Type'].str.upper()

# The name of the table where you want to insert the data
table_name = 'boat_security'

# Write the cleaned and transformed data from the DataFrame to MySQL
df.to_sql(table_name, engine, if_exists='replace', index=False)


# Execute an SQL query to retrieve the data from the MySQL table
sql_query = f'SELECT * FROM {table_name}'
df = pd.read_sql_query(sql_query, engine)

# Specify the path for the output Excel file
output_excel_file = 'Updated_Data_Set.xlsx'

# Save the data from the SQL query to an Excel file
df.to_excel(output_excel_file, index=False)