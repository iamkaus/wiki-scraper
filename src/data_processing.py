import re
import os
import json


def read_raw_data(raw_data_path):
    """
    Reads raw data from a JSON file.

    Args:
        raw_data_path (str): Path to the raw data JSON file.

    Returns:
        list: The existing data as a list of dictionaries.
    """
    if not os.path.exists(raw_data_path):
        raise FileNotFoundError(f"The file {raw_data_path} does not exist.")

    with open(raw_data_path, 'r') as file:
        data = json.load(file)

        if not data or not isinstance(data, list):
            raise ValueError("Invalid or empty data in the raw data file.")

    return data


def clean_summary(summary):
    """
    Cleans a single summary by removing unwanted characters or patterns.

    Args:
        summary (str): The raw summary fetched from Wikipedia.

    Returns:
        str: The cleaned summary.
    """
    if not summary or not isinstance(summary, str):
        raise ValueError("Invalid summary provided for cleaning.")

    # Remove newline characters and extra spaces
    summary = re.sub(r'\s+', ' ', summary).strip()

    # Remove any non-alphanumeric characters except punctuation
    summary = re.sub(r'[^a-zA-Z0-9.,!?\'" ]', '', summary)

    return summary


def process_data(raw_data_path, processed_data_path):
    """
    Processes raw data by cleaning summaries and saving processed summaries to a file.

    Args:
        raw_data_path (str): Path to the raw data JSON file.
        processed_data_path (str): Path to save processed summaries.

    Writes:
        None
    """
    raw_data = read_raw_data(raw_data_path)

    # Clean summaries and prepare processed data
    processed_summaries = [
        clean_summary(item.get("Summary", "")) for item in raw_data
    ]

    # Ensure the processed data directory exists
    os.makedirs(os.path.dirname(processed_data_path), exist_ok=True)

    # Save processed data to a file
    with open(processed_data_path, 'w') as file:
        file.write("\n".join(processed_summaries)) # wrap this within a try/catch for better error handling


def truncate_summary(processed_data_path, output_path, max_length=500):
    """
    Truncates processed summaries to a specified maximum length and saves to an output file.

    Args:
        processed_data_path (str): Path to the processed data file.
        output_path (str): Path to save the truncated summaries.
        max_length (int): Maximum length of each summary.

    Writes:
        None
    """
    if not os.path.exists(processed_data_path):
        raise FileNotFoundError(f"The file {processed_data_path} does not exist.")

    with open(processed_data_path, 'r') as file:
        summaries = file.readlines()

    truncated_summaries = [
        summary[:max_length].rstrip() + "..." if len(summary) > max_length else summary
        for summary in summaries
    ]

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w') as file:
        file.write("\n".join(truncated_summaries))
