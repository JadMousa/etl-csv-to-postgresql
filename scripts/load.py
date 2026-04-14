from scripts.connect_db import get_connection
import logging

def load_data(employees_data):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("TRUNCATE TABLE employees;")

        for _, row in employees_data.iterrows():
            cursor.execute(
                "INSERT INTO employees (name, age, salary) VALUES (%s, %s, %s)",
                (row["name"], row["age"], row["salary"])
            )

        connection.commit()

    except Exception as e:
        connection.rollback()
        logging.error(f"Error loading data: {e}")

    finally:
        cursor.close()
        connection.close()