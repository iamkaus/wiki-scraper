# Wikipedia Scraper

**Wikipedia Scraper** is a Python-based tool designed to scrape summaries of Wikipedia articles. It fetches data from Wikipedia using the MediaWiki API, processes the summaries, and saves them in a structured format for further use. The project also includes features for saving, processing, and truncating the scraped data.

## Features

- Scrapes summaries from Wikipedia articles using their titles.
- Saves raw data in JSON format for future processing.
- Processes data by cleaning and truncating the summaries.
- Supports saving processed data to CSV format.
- Handles errors related to API requests, file I/O, and data processing.

## Tech Stack

- **Python 3.x**
- **Requests**: For making HTTP requests to Wikipedia’s API.
- **BeautifulSoup (bs4)**: For HTML parsing (if used for further scraping).
- **JSON**: For storing raw data.
- **Pandas**: For saving processed data to CSV format.
- **Regex**: For cleaning the scraped summaries.

## Installation

### Prerequisites

Make sure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/) (Python package manager)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/wikipedia-scraper.git
   cd wikipedia-scraper
2. **Set up python virtual environment:**
    ```bash
    python -m venv venv
3. **Activation on Windows:**
    ```bash
    venv\Scripts\activate
4. **Activation on MacOS:**
    ```bash
    source venv/bin/activate
5. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
# Usage
1. **Scraping a Wikipedia Page:**
    To scrape a Wikipedia page summary, you can run the wikipedia_scraper.py make sure to replace the *demo* string in `/src/run.py` `wikipedia_scraper` function with **<valid_wikipedia_article_title>**. For example: **<Artificial_intelligence>**

    ```bash
    python run.py
2. **Alternative approach:**
    To run the scraper program create a `main.py` and import necessary modules from the package `scraper`
    ```bash
    # Import necessary functions from the scraper package
    from scraper import fetch_wikipedia_page, wikipedia_scraper

    # Define the title you want to scrape
    title = "Python_(programming_language)"

    # Fetch and display the summary of the Wikipedia page
    summary = fetch_wikipedia_page(title)
    print("Summary:", summary)

    # Alternatively, use the wikipedia_scraper function to scrape and save data
    data = wikipedia_scraper(title)
    print("Raw Data Scraped:", data)
3. **Run main.py:** 
    Now, you can simply run `main.py` to see the web scraper in action.
    ```bash
    python main.py
# Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please ensure that your code follows the existing style and includes unit tests where applicable.

# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.