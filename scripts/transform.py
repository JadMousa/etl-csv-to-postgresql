def transform_data(employees_data):# increase the data by 10 percent
    employees_data["salary"] = employees_data["salary"] * 1.10
    employees_data["salary"] = employees_data["salary"].round(2)
    return employees_data