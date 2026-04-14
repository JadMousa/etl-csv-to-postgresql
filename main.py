import logging
from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/etl.log"),
        logging.StreamHandler()
    ]
)


def main():
    try:
        logging.info("ETL pipeline started")

        employees_data = extract_data()
        logging.info("CSV extracted successfully")

        employees_data = transform_data(employees_data)
        logging.info("Data transformed successfully")

        load_data(employees_data)
        logging.info("Data loaded into PostgreSQL successfully")

        logging.info("ETL pipeline completed successfully")

    except Exception as e:
        logging.error(f"ETL pipeline failed: {e}")

if __name__ == "__main__":
    main()