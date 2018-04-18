import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GonanceConfig

from datascience.util import make_array
from datascience import Table, CurrencyFormatter, PercentFormatter

scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']
credentials = ServiceAccountCredentials.from_json_keyfile_name(GonanceConfig.OAUTH2_SERVICE_KEY, scope)
gspread_client = gspread.authorize(credentials)

# Example
investion_sheet = gspread_client.open_by_key(GonanceConfig.INVESTION_SHEET_KEY)
investion_historical = investion_sheet.worksheet('Historical')
crowdlending_gsheet = []
crowdlending_gsheet.append(investion_historical.range('A3:A12'))
crowdlending_gsheet.append(investion_historical.range('B3:B12'))
crowdlending_gsheet.append(investion_historical.range('C3:C12'))
crowdlending_gsheet.append(investion_historical.range('D3:D12'))
crowdlending_gsheet.append(investion_historical.range('E3:E12'))
crowdlending_gsheet.append(investion_historical.range('F3:F12'))
crowdlending_gsheet.append(investion_historical.range('G3:G12'))

matrix = []
for column in crowdlending_gsheet:
	matrix.append([])
	for cell in column:
		if '%' in cell.value:
			matrix[len(matrix)-1].append(float(cell.value.replace('%', '').replace(',', '')) / 100)
		elif '€' in cell.value:
			matrix[len(matrix)-1].append(float(cell.value.replace('€', '').replace(',', '')))
		else:
			matrix[len(matrix)-1].append(cell.value)

crowdlending = Table().with_column(
	'Period', matrix[0],
	'Investment', matrix[1],
	'Profit', matrix[2],
	'Estimated Profit', matrix[3],
	'Profit %', matrix[4],
	'Invested', matrix[5],
	'Bank', matrix[6]
	)

crowdlending.set_format([1,2,3,5,6], CurrencyFormatter(symbol='€'))
crowdlending.set_format(4, PercentFormatter)
print('Crowdlending')
print(crowdlending)