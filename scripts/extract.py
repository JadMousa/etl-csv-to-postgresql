import pandas as pd

def extract_data():
    employees_data = pd.read_csv("data/employees.csv")

    if employees_data.empty:
        raise ValueError("CSV file is empty")
   
    return employees_data