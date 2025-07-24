import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from datetime import datetime
import numpy as np
import os # Make sure os is imported

# Define parameters
DATA_URL = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
EXCHANGE_RATE_CSV_PATH = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv"

# Paths for outputs
OUTPUT_DIR = r"C:\Users\PC\Documents\Python course\Project2"
OUTPUT_CSV_FILENAME = "Largest_banks_data.csv"
OUTPUT_CSV_PATH = os.path.join(OUTPUT_DIR, OUTPUT_CSV_FILENAME)

DB_NAME = "Banks.db"
TABLE_NAME = "Largest_banks"
DB_PATH = os.path.join(OUTPUT_DIR, DB_NAME) # Database file path

LOG_FILE = os.path.join(OUTPUT_DIR, "code_log.txt") # Set log file path to the project directory

# Task 1: Logging function
def log_progress(message):
    """
    Logs the progress of the code at different stages in a file code_log.txt.
    """
    timestamp_format = '%Y-%h-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    
    # Ensure log directory exists before writing
    log_dir = os.path.dirname(LOG_FILE)
    os.makedirs(log_dir, exist_ok=True)

    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} : {message}\n")
    print(f"{timestamp} : {message}")

# Task 2: Extraction of data
def extract(url):
    """
    Extracts the table of largest banks by market capitalization from the given URL.
    Returns a Pandas DataFrame with 'Name' and 'MC_USD_Billion' columns.
    Assumes a consistent table structure.
    """
    log_progress("Starting data extraction.")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('span', id='By_market_capitalization').find_next('table')

    data = []
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        name = cols[1].text.strip()
        mc_usd_billion_str = cols[2].text.strip().replace('\n', '')
        mc_usd_billion = float(mc_usd_billion_str)
        data.append({'Name': name, 'MC_USD_Billion': mc_usd_billion})
    
    log_progress("Data extraction complete.")
    return pd.DataFrame(data)

# Task 3: Transformation of data
def transform(df, exchange_rate_path):
    """
    Transforms the DataFrame by adding market capitalization in GBP, EUR, and INR.
    Reads exchange rates from a CSV file.
    """
    log_progress("Starting data transformation.")

    exchange_rates_df = pd.read_csv(exchange_rate_path)
    exchange_rate = exchange_rates_df.set_index('Currency').to_dict()['Rate']

    df['MC_GBP_Billion'] = [np.round(x * exchange_rate['GBP'], 2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x * exchange_rate['EUR'], 2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x * exchange_rate['INR'], 2) for x in df['MC_USD_Billion']]
    
    log_progress("Data transformation complete.")
    return df

# Task 4: Loading to CSV
def load_data(target_filepath, transformed_data):
    """
    Loads the transformed DataFrame to a CSV file.
    Includes error handling for robust logging.
    """
    log_progress(f"Attempting to load data to CSV: {target_filepath}.")
    try:
        target_dir = os.path.dirname(target_filepath)
        os.makedirs(target_dir, exist_ok=True) # Ensure directory exists
        transformed_data.to_csv(target_filepath, index=False)
        log_progress(f"Data successfully loaded to CSV: {target_filepath}")
    except PermissionError as pe:
        log_progress(f"PERMISSION ERROR loading data to CSV {target_filepath}: {pe}")
        log_progress("Please ensure the script has write permissions to the specified directory.")
    except Exception as e:
        log_progress(f"GENERIC ERROR loading data to CSV {target_filepath}: {e}")

# Task 5: Loading to Database
def load_to_db(df, conn, table_name):
    """
    Loads the DataFrame into an SQLite database table.
    """
    log_progress(f"Starting data load to database table: {table_name}.")
    try:
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        log_progress(f"Data successfully loaded to database table: {table_name}")
    except Exception as e:
        log_progress(f"ERROR loading data to database table {table_name}: {e}")

# Task 6: Function to Run queries on Database
def run_queries(query_statement, conn):
    """
    Executes a SQL query on the database and prints the output.
    """
    log_progress(f"Executing query: {query_statement}")
    try:
        query_output_df = pd.read_sql_query(query_statement, conn)
        print(f"\n--- Query: {query_statement} ---")
        print(query_output_df.to_string(index=False))
        log_progress(f"Query executed successfully: {query_statement}")
    except Exception as e:
        log_progress(f"ERROR executing query '{query_statement}': {e}")

# Main execution flow
if __name__ == "__main__":
    # Task 7: Automated log file cleanup
    print("--- Starting ETL Process ---")
    log_progress("Task 7: Checking for and removing old log file.")
    if os.path.exists(LOG_FILE):
        try:
            os.remove(LOG_FILE)
            print(f"Removed old log file: {LOG_FILE}")
        except PermissionError:
            print(f"Warning: Could not remove old log file. It might be open by another process: {LOG_FILE}")
        except Exception as e:
            print(f"Error removing old log file: {e}")
    else:
        print("No old log file found to remove.")
    
    # Now proceed with the actual ETL logging and process
    log_progress("Preliminaries complete. Initiating ETL process.")

    # Task 2: Extraction
    extracted_data = extract(DATA_URL)
    log_progress("Extraction complete.")

    # Task 3: Transformation
    transformed_data = transform(extracted_data, EXCHANGE_RATE_CSV_PATH)
    print("\n--- Transformed Data (Top 10) ---")
    print(transformed_data.head(10).to_string(index=False))
    print(f"\nMarket capitalization of the 5th largest bank (index 4) in billion EUR: {transformed_data['MC_EUR_Billion'][4]}")
    log_progress("Transformation complete.")

    # Task 4: Loading to CSV
    load_data(OUTPUT_CSV_PATH, transformed_data)
    log_progress("Load to CSV phase complete.")

    # Task 5: Loading to Database
    log_progress("Starting database connection and load process.")
    conn = None 
    try:
        db_dir = os.path.dirname(DB_PATH)
        os.makedirs(db_dir, exist_ok=True)
        
        conn = sqlite3.connect(DB_PATH)
        log_progress(f"Database connection established to: {DB_PATH}")

        load_to_db(transformed_data, conn, TABLE_NAME)
        log_progress("Load to Database phase complete.")

        # Task 6: Running queries on the database
        log_progress("Starting database querying phase.")
        
        query_1 = "SELECT * FROM Largest_banks"
        run_queries(query_1, conn)

        query_2 = "SELECT AVG(MC_GBP_Billion) FROM Largest_banks"
        run_queries(query_2, conn)

        query_3 = "SELECT Name from Largest_banks LIMIT 5"
        run_queries(query_3, conn)
        
        log_progress("Database querying phase complete.")

    except Exception as e:
        log_progress(f"ERROR during database operation or query: {e}")
    finally:
        if conn:
            conn.close()
            log_progress("Database connection closed.")
    print("--- ETL Process Complete ---")