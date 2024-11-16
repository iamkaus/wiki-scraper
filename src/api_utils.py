import requests
import os
import json

WIKI_API_URL = "https://en.wikipedia.org/w/api.php"

def fetch_wikipedia_page(title):
    """
    Fetches the summary of a Wikipedia page using the MediaWiki API.

    Args:
        title (str): The title of the Wikipedia page.

    Returns:
        dict: A dictionary containing the page ID and the summary of the Wikipedia page or an error message.

    Raises:
        ValueError: If the title is None or an empty string.
        requests.RequestException: For HTTP or connection-related issues.
    """
    if not title or not title.strip():
        raise ValueError("The title cannot be empty or None. Please provide a valid title.")

    params = {
        'action': 'query',
        'format': 'json',
        'titles': title,
        'prop': 'extracts',
        'exintro': True,
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(WIKI_API_URL, params=params, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()
        pages = data.get('query', {}).get('pages', {})

        if not pages:
            return "No pages found for the given title."

        # Extract page ID and summary
        page = list(pages.values())[0]
        page_id = page.get("pageid", "No page ID found")
        summary = page.get("extract", "No extract available")

        return {"page_id": page_id, "summary": summary}

    except requests.RequestException as e:
        return f"An error occurred while fetching the Wikipedia page: {e}"

def wikipedia_scraper(title):
    """
    Scrapes a Wikipedia page by title, saves raw data to a JSON file.
   
    Raises:
        ValueError: If the title is invalid.
        IOError: If there are issues with file operations.
    """

    if not title or not title.strip():
        raise ValueError("The title cannot be empty or None. Please provide a valid title.")

    # Fetch the Wikipedia page summary and page ID
    result = fetch_wikipedia_page(title)

    if isinstance(result, str):
        # Handle error message if any
        raise ValueError(result)

    page_id = result.get("page_id")
    summary = result.get("summary")

    # Prepare raw data
    raw_data = {"Title": title, "Page_ID": page_id, "Summary": summary}

    # File path for raw data
    raw_data_path = 'data/raw_data/raw_data.json'

    # Ensure the raw data directory exists
    os.makedirs(os.path.dirname(raw_data_path), exist_ok=True)

    try:
        # Check if the file exists and is not empty
        if os.path.exists(raw_data_path) and os.path.getsize(raw_data_path) > 0:
            with open(raw_data_path, 'r+') as file:
                existing_data = json.load(file)

                # Ensure it's a valid list
                if not isinstance(existing_data, list):
                    raise ValueError("The raw data file does not contain a valid list.")

                # Avoid duplicates
                if raw_data not in existing_data:
                    existing_data.append(raw_data)
                    file.seek(0)
                    json.dump(existing_data, file, indent=4)
                    file.truncate()
        else:
            # Create a new JSON file
            with open(raw_data_path, 'w') as file:
                json.dump([raw_data], file, indent=4)

    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

    return raw_data


# Example usage:
if __name__ == "__main__":
    try:
        result = wikipedia_scraper("Python_(programming_language)")
        print("Scraped data:", result)
    except Exception as e:
        print(f"An error occurred: {e}")
