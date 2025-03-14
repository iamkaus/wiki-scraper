from scraper import wikipedia_scraper
from data_processing import process_data, truncate_summary
from storage import save_to_csv
import os


def main():
    # Create base directory paths
    base_dir = os.path.join(os.getcwd(), "wiki-scraper")
    os.makedirs(base_dir, exist_ok=True)

    # Define file paths
    html_data_path = os.path.join(base_dir, "html_data.txt")
    processed_data_path = os.path.join(base_dir, "processed_data.txt")
    processed_output_data_path = os.path.join(base_dir, "processed_output_data.txt")
    processed_csv_data_path = os.path.join(base_dir, "processed_csv_data.csv")

    wikipedia_scraper('Machine_code')

    process_data(html_data_path, processed_data_path)

    truncate_summary(processed_data_path, processed_output_data_path, 300)

    save_to_csv(processed_output_data_path, processed_csv_data_path)


if __name__ == "__main__":
    main()