# ETL Pipeline (CSV to PostgreSQL)

## Overview

This project implements a simple ETL (Extract, Transform, Load) pipeline in Python.
It reads employee data from a CSV file, applies transformations, and loads the processed data into a PostgreSQL database.

---

## Features

* Extract data from CSV using Pandas
* Transform data (salary increase by 10%)
* Load data into PostgreSQL
* Logging of pipeline execution
* Environment-based database configuration (.env)

---

## Project Structure

```
├── data/
│   └── employees.csv
├── logs/
│   └── etl.log
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── connect_db.py
├── main.py
├── requirements.txt
├── .gitignore
└── .env (not included)
```

---

## How It Works

1. **Extract**
   Reads employee data from `data/employees.csv`

2. **Transform**
   Increases salary by 10% and rounds to 2 decimal places

3. **Load**
   Inserts data into PostgreSQL after truncating the table

---

## Setup Instructions

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Configure environment variables

Create a `.env` file:

```
DB_HOST=localhost
DB_NAME=company
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5432
```

### 3. Run the pipeline

```
python main.py
```

---

## Sample Data

```
name,age,salary
Sam,25,3000
Ali,30,4000
Lina,28,3500
```

---

## Notes

* The pipeline truncates the table before loading data
* Logging is stored in `logs/etl.log`
* `.env` file is ignored for security reasons

---

## Future Improvements

* Batch insert (executemany) for performance
* Data validation and schema checks
* Scheduling (cron job)
* Support for multiple data sources

---

## Technologies Used

* Python
* Pandas
* PostgreSQL
* psycopg2
