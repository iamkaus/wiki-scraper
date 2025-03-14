import json
import pandas as pd
import os


def save_to_csv(path, processed_csv_data_path):
    """
    Saves data from a text file to a CSV file.

    Args:
        path (str): Path to the text file containing one summary per line.
        processed_csv_data_path (str): Path where the CSV will be saved.
    """
    try:
        # Check if input file exists
        if not os.path.exists(path):
            raise FileNotFoundError(f"The file {path} does not exist.")

        # Read the text file
        with open(path, 'r') as file:
            summaries = [line.strip() for line in file.readlines() if line.strip()]

        if not summaries:
            raise ValueError("No data found in the input file.")

        # Create a dictionary for the DataFrame
        data = [{"Summary": summary} for summary in summaries]

        # Validate file path
        if not processed_csv_data_path.endswith('.csv'):
            raise ValueError("The provided path is not a valid CSV file path.")

        # Ensure directory exists
        os.makedirs(os.path.dirname(processed_csv_data_path), exist_ok=True)

        # Create and save DataFrame
        df = pd.DataFrame(data)
        df.to_csv(processed_csv_data_path, index=False)

        print(f"CSV successfully created at {processed_csv_data_path}")

    except Exception as e:
        print(f"Error creating CSV: {e}")