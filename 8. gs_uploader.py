from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import numpy as np

SERVICE_ACCOUNT_FILE = '________________.json'
SCOPES = ['_______________________________________________']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '_________________________________________'

# Call the Sheets API
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

file = '_____________'
df = pd.read_csv(file)
df.replace(np.nan, '', inplace=True)


to_update = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                           range="A:H", valueInputOption="USER_ENTERED", body={"values":df.T.reset_index().T.values.tolist()}).execute()  ###不如予位置就會自動產生(A1:B4最後的位)
                            ###開新table要用service, 不可以在此增加