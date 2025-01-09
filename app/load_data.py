import os
import pandas as pd
from sqlalchemy import create_engine

excel_file = os.path.abspath('20210309_2020_1 - 4 (1) (1) (1) (1).xls')  # Excel file path
sheet_name = 'Sheet1'  # sheet name 
database_name = 'ohio_oil.db'  
table_name = 'wells'


try:
    print(excel_file)
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    engine = create_engine(f'sqlite:///{database_name}', echo=True)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Data loaded into {database_name} in table {table_name}")
except PermissionError as pe:
    print(f" PermissionError: {pe}")
except Exception as ex:
    print(f"Error: {ex}")
