import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
import logging 


log_file = "log_file.txt"
target_file = "transformed_data.csv"

HEADERS = ["car_model", "year_of_manufacture", "price", "fuel"]


# The format includes timestamp, log level, and message.
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def log_progress(message):
    """
    Logs a message with a timestamp to the log file and the console.
    """
    # Use logging.info to record informational messages
    logging.info(message)
    # Also print to console for immediate feedback
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] INFO: {message}")

# --- EXTRACTION FUNCTIONS  ---

def extract_from_csv(file_to_process):
    
   # Extracts data from a CSV file and returns a pandas DataFrame.
    #Ensures that only the columns required by HEADERS are extracted.
    
    try:
        # pd.read_csv will read the file specified by 'file_to_process'
        dataframe = pd.read_csv(file_to_process)
        df_selected = dataframe[HEADERS]
        log_progress(f"Data extracted from CSV: {file_to_process}")
        return df_selected
    except FileNotFoundError:
        log_progress(f"ERROR: CSV file not found: {file_to_process}")
        return pd.DataFrame(columns=HEADERS) # Returns an empty DataFrame with expected columns
    except KeyError as e:
        log_progress(f"ERROR: Expected columns not found in CSV {file_to_process}: {e}. Ensure CSV has columns: {HEADERS}")
        return pd.DataFrame(columns=HEADERS)
    except Exception as e:
        log_progress(f"UNEXPECTED ERROR extracting from CSV {file_to_process}: {e}")
        return pd.DataFrame(columns=HEADERS)

def extract_from_json(file_to_process):
    
   # Extracts data from a JSON file (assuming line-delimited format) and returns a pandas DataFrame.
    #Ensures that only the columns required by HEADERS are extracted.
    
    try:
        # Assuming JSON is in a line-delimited object format, as in the original exercise.
        # If it were an array of JSON objects, 'lines=True' would not be necessary.
        dataframe = pd.read_json(file_to_process, lines=True)
        
        # Select only the columns we need
        df_selected = dataframe[HEADERS]
        log_progress(f"Data extracted from JSON: {file_to_process}")
        return df_selected
    except FileNotFoundError:
        log_progress(f"ERROR: JSON file not found: {file_to_process}")
        return pd.DataFrame(columns=HEADERS)
    except KeyError as e:
        log_progress(f"ERROR: Expected columns not found in JSON {file_to_process}: {e}. Ensure JSON has columns: {HEADERS}")
        return pd.DataFrame(columns=HEADERS)
    except Exception as e:
        log_progress(f"UNEXPECTED ERROR extracting from JSON {file_to_process}: {e}")
        return pd.DataFrame(columns=HEADERS)

def extract_from_xml(file_to_process):
    
   # Extracts data from an XML file and returns a pandas DataFrame.
    
    extracted_data_list = [] # List to store dictionaries of data for each car
    try:
        tree = ET.parse(file_to_process)
        root = tree.getroot() # The root element of the XML document
        
       
        for car_element in root.findall('car'): # Assuming each car is within a <car> element
            # Extract the text of each sub-element. Use .text to get content,
            # and None if the element doesn't exist to prevent errors.
            car_model = car_element.find('car_model').text if car_element.find('car_model') is not None else None
            year_of_manufacture = car_element.find('year_of_manufacture').text if car_element.find('year_of_manufacture') is not None else None
            price = car_element.find('price').text if car_element.find('price') is not None else None
            fuel = car_element.find('fuel').text if car_element.find('fuel') is not None else None
            
            
            try:
                year_of_manufacture = int(year_of_manufacture) if year_of_manufacture else None
            except (ValueError, TypeError):
                year_of_manufacture = None # If it cannot be converted to int, assign None

            try:
                price = float(price) if price else None
            except (ValueError, TypeError):
                price = None # If it cannot be converted to float, assign None

            # Add a dictionary with the car's data to the list
            extracted_data_list.append({
                "car_model": car_model,
                "year_of_manufacture": year_of_manufacture,
                "price": price,
                "fuel": fuel
            })
        
        # Create a pandas DataFrame from the list of dictionaries, ensuring correct columns
        dataframe = pd.DataFrame(extracted_data_list, columns=HEADERS)
        log_progress(f"Data extracted from XML: {file_to_process}")
        return dataframe
    except FileNotFoundError:
        log_progress(f"ERROR: XML file not found: {file_to_process}")
        return pd.DataFrame(columns=HEADERS)
    except Exception as e:
        log_progress(f"UNEXPECTED ERROR extracting from XML {file_to_process}: {e}")
        return pd.DataFrame(columns=HEADERS)


def extract():
    
    #Combines data extraction from all CSV, JSON, and XML files
    #in the SOURCE_FOLDER. Returns a single consolidated DataFrame.
    
    log_progress("Starting Extraction phase.")
    # Initialize an empty DataFrame with the expected final columns
    extracted_data = pd.DataFrame(columns=HEADERS)

    
    for csvfile in glob.glob(SOURCE_FOLDER + "*.csv"):
        # Ensure the CSV file is not the transformed target file 
        if SOURCE_FOLDER + target_file not in csvfile: # Compare the full path
            df_csv = extract_from_csv(csvfile)
            # Concatenate the extracted DataFrame if it's not empty
            if not df_csv.empty:
                extracted_data = pd.concat([extracted_data, df_csv], ignore_index=True)

    # Process all JSON files in the SOURCE_FOLDER
    for jsonfile in glob.glob(SOURCE_FOLDER + "*.json"):
        df_json = extract_from_json(jsonfile)
        if not df_json.empty:
            extracted_data = pd.concat([extracted_data, df_json], ignore_index=True)

    # Process all XML files in the SOURCE_FOLDER
    for xmlfile in glob.glob(SOURCE_FOLDER + "*.xml"):
        df_xml = extract_from_xml(xmlfile)
        if not df_xml.empty:
            extracted_data = pd.concat([extracted_data, df_xml], ignore_index=True)

    log_progress("Extraction phase completed.")
    return extracted_data

# --- TRANSFORMATION FUNCTION OF CURRENCY ---
def transform(data):
    
   # Transforms the data DataFrame:
    #- Rounds the 'price' column values to 2 decimal places.
    
    log_progress("Starting Transformation phase.")
    
    # Convert to float, using 'coerce' to convert non-numeric values to NaN (Not a Number)
    data['price'] = pd.to_numeric(data['price'], errors='coerce')
    data['price'] = data['price'].round(2)
    
    log_progress("Transformation phase completed.")
    return data

# --- LOAD FUNCTION  ---
def load_data(target_filepath, transformed_data):
    
    log_progress("Starting Load phase.")
    try:
        # to_csv saves the DataFrame to a CSV file.
        
        transformed_data.to_csv(target_filepath, index=False)
        log_progress(f"Data successfully loaded to: {target_filepath}")
    except Exception as e:
        log_progress(f"ERROR loading data to {target_filepath}: {e}")

# ---  Test  ---
if __name__ == "__main__":
    log_progress("ETL Job Started.")

    # Extraction Phase
    log_progress("Extraction phase initiated.")
    extracted_data = extract()
    log_progress("Extraction phase finished.")
    print("\n--- Extracted Data (first 5 rows) ---")
    print(extracted_data.head())
    print(f"Total rows extracted: {len(extracted_data)}")

    # Transformation Phase
    log_progress("Transformation phase initiated.")
    transformed_data = transform(extracted_data)
    log_progress("Transformation phase finished.")
    print("\n--- Transformed Data (first 5 rows) ---")
    print(transformed_data.head())
    print(f"Total rows transformed: {len(transformed_data)}")

    # Load Phase
    log_progress("Load phase initiated.")
    load_data(target_file, transformed_data)
    log_progress("Load phase finished.")

    log_progress("ETL Job Completed Successfully.")

