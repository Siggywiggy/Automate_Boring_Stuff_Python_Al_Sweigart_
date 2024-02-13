import openpyxl
workbook = openpyxl.load_workbook('example.xlsx')

print(workbook.sheetnames) # The workbook's sheets' names.
sheet_3 = workbook['Sheet3'] # Get a sheet from the workbook.
print(sheet_3)
print(type(sheet_3))
print(sheet_3.title) # Get the sheet's title as a string.

another_sheet = workbook.active # Get the active sheet.
print(another_sheet)