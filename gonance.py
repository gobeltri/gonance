import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GonanceConfig

scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']
credentials = ServiceAccountCredentials.from_json_keyfile_name(GonanceConfig.OAUTH2_SERVICE_KEY, scope)
gspread_client = gspread.authorize(credentials)

# Example
investion_sheet = gspread_client.open_by_key(GonanceConfig.INVESTION_SHEET_KEY)
investion_historical = investion_sheet.worksheet('Historical')
cell_list = investion_historical.range('B3:B12')
for cell in cell_list:
    print(cell.value)

