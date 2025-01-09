import os
import pandas as pd
from sqlalchemy import create_engine

excel_file = os.path.abspath('20210309_2020_1 - 4 (1) (1) (1) (1).xls')  # Excel file path
sheet_name = 'Sheet1'  # sheet name 
database_name = os.path.abspath('app/ohio_oil.db')
table_name = 'wells'


try:
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    engine = create_engine(f'sqlite:///{database_name}', echo=True)
    # modify excel headers to model fields
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    if 'quarter_1,2,3,4' in df.columns:
        df.rename(columns={'quarter_1,2,3,4': 'quarter'}, inplace=True)
    annual_data = df.groupby('api_well__number').agg({
        'oil': 'sum',
        'gas': 'sum',
        'brine': 'sum',
    }).reset_index()

    # Add other necessary columns if needed
    # annual_data['production_year'] = df['production_year'].unique()[0]        
    annual_data.to_sql(table_name, con=engine, if_exists='append', index=False)
    print(f"Data loaded into {database_name} in table {table_name}")
except PermissionError as pe:
    print(f" PermissionError: {pe}")
except Exception as ex:
    print(f"Error: {ex}")
