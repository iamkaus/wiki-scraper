from scraper import wikipedia_scraper
from data_processing import process_data, truncate_summary
from storage import save_to_csv

def main():
    # Step 1: Scrape data from Wikipedia
    raw_data = wikipedia_scraper("<WIKI_VALID_TITLE>") # replace with wiki valid title

    # Step 2: Process the raw data and clean the summaries
    process_data("<RAW_DATA_PATH>", "<PROCESSED_DATA_PATH>")

    # Step 3: Optionally truncate the summaries to a specified length
    truncate_summary("<RAW_DATA_PATH>", "<PROCESSED_DATA_PATH>" "<MAX_LENGTH (default parameter)>") # replace strings with appropriate paths and default parameter

    # Step 4: Save the processed data to CSV
    save_to_csv(raw_data, "<PROCESSED_CSV_DATA_PATH>") # replace with processed_csv_data path


if __name__ == "__main__":
    main()