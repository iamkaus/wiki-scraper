from api_utils import fetch_wikipedia_page
import os
import json
from bs4 import BeautifulSoup


def wikipedia_scraper(title):
    """
    Scrapes a Wikipedia page by title, saves raw data to a JSON file.
    Now extracts text from HTML and structures data as a list of dictionaries.
   
    Raises:
        ValueError: If the title is invalid.
        IOError: If there are issues with file operations.
    """

    # Validate title
    if not title or not title.strip():
        raise ValueError("The title cannot be empty or None. Please provide a valid title.")

    # Fetch the Wikipedia page summary
    raw_html = fetch_wikipedia_page(title)

    if not raw_html:
        raise ValueError(f"No summary available for the title '{title}'.")

    # Parse HTML and extract text
    soup = BeautifulSoup(raw_html, 'html.parser')
    summary = soup.get_text(separator=' ', strip=True)

    # Create the structured data as a list of dictionaries
    raw_data = [{"Title": title, "Summary": summary}]

    # File path for raw data
    raw_data_path = '<raw_data_path>' # replace with path where raw_data should dump in

    # Ensure the raw data directory exists
    os.makedirs(os.path.dirname(raw_data_path), exist_ok=True)

    # Save raw data to a JSON file
    try:
        # Check if the file exists and is not empty
        if os.path.exists(raw_data_path) and os.path.getsize(raw_data_path) > 0:
            with open(raw_data_path, 'r+') as file:
                try:
                    existing_data = json.load(file)

                    # Ensure it's a valid list
                    if not isinstance(existing_data, list):
                        raise ValueError("The raw data file does not contain a valid list.")

                    # Avoid duplicates
                    if raw_data not in existing_data:
                        existing_data.append(raw_data[0])
                        file.seek(0)
                        json.dump(existing_data, file, indent=4)
                        file.truncate()
                except json.JSONDecodeError:
                    # Handle corrupted JSON file
                    print("Corrupted JSON file. Rewriting with new data.")
                    with open(raw_data_path, 'w') as new_file:
                        json.dump([raw_data[0]], new_file, indent=4)
        else:
            # Create a new JSON file
            with open(raw_data_path, 'w') as file:
                json.dump([raw_data[0]], file, indent=4)

    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

    return raw_data


# Example Usage -> only for test
if __name__ == "__main__":
    try:
        wikipedia_scraper("Python_(programming_language)")
    except Exception as e:
        print(f"An error occurred: {e}")
