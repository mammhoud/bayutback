# Bayut Website Web Scraping and Crawling

This repository demonstrates the use of Selenium for web scraping and crawling on the Bayut website, allowing users to collect property listings, transactions, and other relevant data. The application features an integrated database to store, manage, and query data quickly and efficiently.

## Project Structure

The repository is organized into several key components to handle the web scraping, data storage, and querying tasks:

### Files and Directories Overview
```
├── db
│   ├── Files
│   │   ├── Loaded_PDF
│   │   │   └── *.csv                         # CSV files scraped from PDFs
│   │   └── [location]
│   │       └── [date]_PropertisListing.csv    # CSV files of property listings based on location and date
│   ├── db.sqlite3                             # SQLite database file
│   └── models.py                              # Database model to store scraped data
├── elements.py                                # Web elements used for scraping
├── main.py                                    # Main script for user input and data extraction
├── manage.py                                  # Django app initialization for ORM usage
├── requirements.txt                           # Required Python packages for the project
├── scrapPDF.py                                # Script for scraping PDF files
├── scrapProperties.py                         # Script for scraping property data
├── scrapTransactions.py                       # Script for scraping transaction data
├── searchFields.py                            # Fields used for searching/filtering properties
├── searchPropertiesListing.py                 # Handles searching property listings
└── utils
    ├── __init__.py
    ├── dateValidations.py                     # Utility functions for date validation
    ├── load_File.py                           # Utility functions to load data files
    ├── save_Data.py                           # Utility functions to save data into files and database
    └── webDriver.py                           # WebDriver initialization and settings
```

### Key Components

1. **`db/`**: 
   - **Files/Loaded_PDF/**: Directory to store CSV files generated from scraping PDFs.
   - **Files/[location]/**: Organized by location and date, storing property listings in CSV format.
   - **db.sqlite3**: The SQLite database that stores data collected from the website.
   - **models.py**: Contains Django ORM models for faster data querying and storage.

2. **`elements.py`**:
   - Defines the web elements (such as buttons, input fields, etc.) used by Selenium to interact with the Bayut website during the scraping process.

3. **`main.py`**:
   - The main entry point for the user to initiate searches on the Bayut website, scrape the data, and save it into CSV files and the SQLite database.
   
4. **`manage.py`**:
   - A Django management file, used for database migrations and ORM-related commands.

5. **`scrapPDF.py`**:
   - Script to scrape and parse data from PDFs related to property transactions or listings.

6. **`scrapProperties.py`**:
   - Script responsible for scraping property listing data from Bayut, storing it in a structured format.

7. **`scrapTransactions.py`**:
   - Script to scrape property transaction details, such as sales or rental prices.

8. **`searchFields.py`**:
   - Defines fields and parameters used to search for specific property listings on the Bayut website.

9. **`searchPropertiesListing.py`**:
   - Contains the logic for handling and filtering property listings based on user input.

10. **`utils/`**:
    - **dateValidations.py**: Contains functions to validate date formats and ranges.
    - **load_File.py**: Loads existing data files into the database.
    - **save_Data.py**: Handles saving scraped data into both files and the database.
    - **webDriver.py**: Sets up and configures Selenium WebDriver for web scraping.

### Installation and Setup

1. **Install Required Packages**:
   To run the project, you'll need to install the required Python packages. You can do this by running:
   ```bash
   pip install -r requirements.txt
   ```

2. **Database Setup**:
   The project uses SQLite for database storage. To initialize the database, run:
   ```bash
   python manage.py migrate
   ```

3. **Selenium WebDriver**:
   The project uses Selenium for web scraping, which requires the appropriate WebDriver for your browser (e.g., ChromeDriver for Google Chrome). Make sure to install and configure it before running the scripts.
   You can download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

   Make sure the WebDriver is added to your system path or configure the path in the `webDriver.py` file.

### Usage

1. **Run the Main Script**:
   To start scraping property listings, use the `main.py` script:
   ```bash
   python main.py
   ```
   You'll be prompted to input search criteria, and the script will scrape the relevant data from the Bayut website. The data is then saved into CSV files and the SQLite database.

2. **Search Property Listings**:
   After the data is scraped and stored, you can use the Django ORM to search and query property listings efficiently through the database.

### Features

- **PDF Scraping**: Automatically parses and extracts data from PDFs related to property transactions or listings.
- **Property Listings Scraping**: Extracts detailed property data, including location, price, size, and more from the Bayut website.
- **Transaction Data Scraping**: Collects and organizes transaction-related data such as sale or rental prices.
- **Data Storage**: All scraped data is saved both in CSV files and in an SQLite database for fast querying.
- **Search Functionality**: Offers the ability to search property listings based on multiple filters such as location, price, and property type.

### Technologies Used

- **Python**: The core programming language used for the project.
- **Selenium**: Used for interacting with the Bayut website and automating data extraction.
- **Django ORM**: For managing the database models and performing efficient data queries.
- **SQLite**: Database used to store scraped data.
- **Pandas**: Used for handling CSV files and data manipulation.

### Future Enhancements

- **Enhance Search Capabilities**: Add more advanced filtering options for property listings.
- **Support for Other Formats**: Implement support for additional file formats like Excel for data storage.
- **Data Visualization**: Add data visualization tools to analyze trends in property listings and transactions.

### Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions for improvement.
---
