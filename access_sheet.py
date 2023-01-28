# code by Prafulla Dalvi
# found @ https://medium.com/analytics-vidhya/how-to-read-and-write-data-to-google-spreadsheet-using-python-ebf54d51a72c

import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow, Flow
from google.auth.transport.requests import Request
import os
import pickle
import branch1_env_pycharm as b1

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# here enter the id of your google sheet
SPREADSHEET_ID_input = os.environ['spreadsheet_id']
RANGE_NAME = 'A1:K33'

def main():
    global values_input, service
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            file_name = os.environ['json_file_name']
            flow = InstalledAppFlow.from_client_secrets_file(
                file_name, SCOPES) # here enter the name of your downloaded JSON file
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result_input = sheet.values().get(spreadsheetId=SPREADSHEET_ID_input,
                                range=RANGE_NAME).execute()
    values_input = result_input.get('values', [])

    if not values_input and not values_expansion:
        print('No data found.')


main()

# df of movie features
df = pd.DataFrame(values_input[1:], columns=values_input[0])


def build_df(df):
    # loop through each row
    for index in df.index:
        attempts = 0
        title = df.loc[index, "title"]
        # not all release dates are in df, either use what is there or ask for it
        if df.loc[index, "release_date"]:
            release_date = df.loc[index, "release_date"]
        else:
            print(title)
            release_date = input("provide release date: ")

        # search API for movie details
        search_results = b1.API_queries().search(title)

        # loop through search results
        for hit in search_results:
            # if search result matches the movie in the df
            if hit["release_date"][:4] == release_date:
                headers = list(df.columns)
                for key in hit:
                    if key in headers:
                        df.loc[index, key] = hit[key]
                break

        # safety net
        attempts += 1
        if attempts < 3:
            if input("continue (y/n)? ") == "n":
                return
    return