# import requests
# from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up Google Sheets API credentials
scope = ['https://www.googleapis.com/auth/spreadsheets']
credential = ServiceAccountCredentials.from_json_keyfile_name("credential.json", scope)
client = gspread.authorize(credential)

# Open the sheet
SHEET_URL = os.getenv("SHEET_URL")
sheet = client.open_by_url(SHEET_URL).sheet1

# Example data to input into the sheet
# This is a list of lists, where each inner list represents a row,
# and each element in the inner list represents a column value for that row.
data_to_input = [
    ["Name", "Age", "City"],  # First row: Column headers
    ["Alice", 30, "New York"],  # Second row: Data
    ["Bob", 25, "Los Angeles"],  # Third row: Data
    # Add more rows as needed
]

# Loop through each row in the data
for row_index, row in enumerate(data_to_input, start=1):  # start=1 because sheet rows and columns are 1-indexed
    # Loop through each column value in the row
    for col_index, value in enumerate(row, start=1):  # start=1 for the same reason
        # Update the cell at the current row and column with the current value
        sheet.update_cell(row_index, col_index, value)

# Print a message to indicate completion
print("Data input complete.")

