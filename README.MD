# Wikipedia Scraper

A Python application that scrapes, processes, and stores Wikipedia article summaries. This tool fetches introductory sections of Wikipedia articles, cleans the text, truncates it to a manageable length, and saves the results in both text and CSV formats.

## Overview

This project demonstrates a complete data pipeline for extracting and processing Wikipedia content:

1. **Data Collection**: Fetch article summaries from Wikipedia using the MediaWiki API
2. **Data Processing**: Clean and format the text content
3. **Data Transformation**: Truncate summaries to specified lengths
4. **Data Storage**: Save processed data in multiple formats (JSON, text, CSV)

## Project Structure

```
wiki-scraper/
    src/
        ├── api_utils.py      # Wikipedia API interaction functions
        ├── scraper.py        # Main scraping functionality
        ├── data_processing.py # Text processing and cleaning functions
        ├── storage.py        # Data storage utilities
        ├── run.py            # Main execution script
└── .gitignore
└── LICENSE           # LICENSE
└── README.md         # Project documentation
```

## Features

- Fetch Wikipedia article introductions by title
- Clean HTML content and extract plain text
- Remove unwanted characters and normalize spacing
- Truncate summaries to configurable lengths
- Export data to CSV for further analysis
- Robust error handling and validation

## Requirements

- Python 3.7+
- BeautifulSoup4
- Requests
- Pandas

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/iamkaus/wiki-scraper.git
   cd wiki-scraper
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   # On Windows
   env\Scripts\activate
   # On macOS/Linux
   source env/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

## Usage

### Basic Usage

Run the scraper with the default configuration:

```bash
python run.py
```

This will:
1. Scrape the "Machine_code" Wikipedia article
2. Process and clean the text
3. Truncate summaries to 300 characters
4. Save results to CSV

### Custom Scraping

To scrape different articles, modify the `title` parameter in `run.py`:

```python
# In run.py
wikipedia_scraper('Python_(programming_language)')  # Replace with any Wikipedia article title
```

### Configuration

Adjust the following parameters to customize behavior:

- **Truncation length**: Change the max_length parameter in `truncate_summary()` call
- **Output paths**: Modify the file paths in `main()` function

## How It Works

### 1. Data Collection (`api_utils.py`)

The `fetch_wikipedia_page()` function uses the MediaWiki API to retrieve article content:

```python
params = {
    'action': 'query',
    'format': 'json',
    'titles': title,
    'prop': 'extracts',
    'exintro': True,
}
```

The `exintro` parameter specifically requests only the introduction section.

### 2. Scraping (`scraper.py`)

The `wikipedia_scraper()` function:
- Validates the article title
- Calls the Wikipedia API
- Parses HTML using BeautifulSoup
- Extracts clean text content
- Saves the raw data as JSON

### 3. Data Processing (`data_processing.py`)

Text processing is handled by two main functions:

- `clean_summary()`: Removes extra spaces, normalizes whitespace, and filters characters
- `process_data()`: Applies cleaning to all scraped summaries

### 4. Truncation (`data_processing.py`)

The `truncate_summary()` function:
- Reads processed summaries
- Truncates each to the specified length
- Adds ellipsis ("...") if truncation occurred
- Saves shortened summaries to a new file

### 5. CSV Export (`storage.py`)

The `save_to_csv()` function:
- Reads the processed text data
- Creates a pandas DataFrame
- Exports to CSV format for analysis

## Error Handling

The application includes comprehensive error handling:

- Input validation for Wikipedia titles
- HTTP request error management
- File I/O exception handling
- Data format validation
- Directory creation for output files

## Troubleshooting

### Common Issues

1. **File Not Found Errors**: Ensure all directories in the file paths exist.
2. **API Rate Limiting**: If you receive HTTP 429 errors, reduce request frequency.
3. **Invalid JSON**: Check that text files aren't being processed as JSON.

### Debugging

Add these print statements to debug file operations:

```python
print(f"File exists: {os.path.exists(path)}")
print(f"File size: {os.path.getsize(path) if os.path.exists(path) else 'N/A'}")
print(f"Current working directory: {os.getcwd()}")
```

## Extension Possibilities

- Add command-line arguments for article selection
- Implement batch processing for multiple articles
- Include additional Wikipedia content (not just introductions)
- Add NLP processing for text analysis
- Create a simple web interface

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.