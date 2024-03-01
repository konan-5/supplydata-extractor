import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv
import time
# Load environment variables
load_dotenv()

# Set up Google Sheets API credentials
scope = ['https://www.googleapis.com/auth/spreadsheets']
credential = ServiceAccountCredentials.from_json_keyfile_name("credential.json", scope)
client = gspread.authorize(credential)

# Open the sheet
SHEET_URL = os.getenv("SHEET_URL")
sheet = client.open_by_url(SHEET_URL).sheet1

file_path = 'urls.txt'

# Open the file and read its contents
with open(file_path, 'r') as file:
    # Loop through each line in the file
    for idx, line in enumerate(file, start=1):  # start=1 begins the index from 1 instead of Python's default 0
        # Each 'line' is a URL in this context, so you can process it here
        url = line.strip() # Remove any leading/trailing whitespace

        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                try:
                    soup = BeautifulSoup(resp.content, features="html.parser")
                    # Using 'string' instead of 'text' to comply with the updated BeautifulSoup syntax
                    detailed_description = soup.find(string="Detailed description:").find_next().text.strip()

                    awarded_supplier = soup.find(string="Awarded supplier:").find_next().text.strip()
                    sheet.append_row([url,detailed_description,awarded_supplier])
                except Exception as e:
                    sheet.append_row([url,"",""])
            else:
                # Append a row with the URL and error messages if the status code is not 200
                sheet.append_row([url,"",""])
        except Exception as e:
            # Append a row with the URL and exception message if an error occurs
            sheet.append_row([url, "", ""])
        finally :
            time.sleep(5)
            print(f"Done: {idx}")
