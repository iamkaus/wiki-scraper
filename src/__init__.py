# Import key functions from the package modules

# Fetching data
from .api_utils import fetch_wikipedia_page

# Processing data
from .data_processing import process_data, truncate_summary

# Saving data
from .storage import save_to_csv

# Define the package's public interface
__all__ = [
    "fetch_wikipedia_page",
    "process_data",
    "truncate_summary",
    "save_to_csv",
]

# Metadata for the package
__version__ = "1.0.0"
__author__ = "Your Name"
__description__ = "A package for scraping, processing, and storing Wikipedia data"
