# EU-SupplyDataExtractor

This Python script is designed to automate the extraction of specific information from web pages on the "https://irl.eu-supply.com/" website and update a Google Sheet with this data. It's crafted to assist in collecting and organizing procurement data, such as detailed descriptions and awarded suppliers, into a centralized spreadsheet for further analysis or record-keeping.

## Features

- **Targeted Data Extraction**: Efficiently extracts detailed descriptions and awarded supplier information from listed procurement URLs.
- **Seamless Google Sheets Integration**: Automatically populates a Google Sheet with the extracted data for easy access and analysis.
- **Considerate Scraping Practices**: Implements a delay between requests to minimize the risk of server overload and ensure compliance with web scraping best practices.

## Prerequisites

To effectively use this script, you must have:

1. **Google Cloud Platform Setup**: A Google Cloud Platform project with the Google Sheets API enabled and a service account created. The credentials file (`credentials.json`) must be downloaded.
2. **Environment Configuration**: A `.env` file to securely store your Google Sheet's URL.
3. **Python Setup**: Python 3.x installed along with necessary dependencies outlined in `requirements.txt`.

## Installation

Follow these steps to get started:

1. Clone the repository to your local machine.
2. Install Python dependencies using pip:
    ```sh
    pip install -r requirements.txt
    ```
3. Place your `credentials.json` file in the project's root directory.
4. Set up a `.env` file in the project root with the following content:
    ```plaintext
    SHEET_URL='your_google_sheet_url_here'
    ```

## Usage

To use the script:

1. Populate `urls.txt` with the URLs you intend to scrape, ensuring one URL per line.
2. Execute the script with:
    ```sh
    python main.py
    ```
3. After the script completes, check the specified Google Sheet for your data.

## Contributing

Your contributions are welcome! If you have suggestions for improving this script or expanding its capabilities, please fork this repository, make your changes, and submit a pull request.

## License

This project is released under the MIT License, making it open-source and freely available for modification and distribution.
