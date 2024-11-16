import pandas as pd
import os

def save_to_csv(data, path):
    """
    Saves the provided data to a CSV file at the specified path.

    Args:
        data (list of dict): Data to be written to the CSV file.
        path (str): The file path where the CSV will be saved. Defaults to 'data/processed_data/processed_data.csv'.

    Raises:
        ValueError: If the data is empty or invalid.
        ValueError: If the path is not a valid CSV path.
        IOError: If there are issues writing to the file.
    """

    try:
        # Validate data
        if not data or not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
            raise ValueError("The data provided is empty or not a valid list of dictionaries.")

        # Validate file path
        if not path.endswith('.csv'):
            raise ValueError("The provided path is not a valid CSV file path.")

        # Ensure the directory exists
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Convert the data into a DataFrame
        data_frame = pd.DataFrame(data)

        # Save the DataFrame to the specified CSV file path
        data_frame.to_csv(path, index=False)

        print(f"Processed data has been successfully saved to {path}")

    except ValueError as ve:
        print(f"Validation Error: {ve}")

    except IOError as ioe:
        print(f"File Writing Error: {ioe}")

    except Exception as error:
        print(f"An unexpected error occurred: {repr(error)}")
