import openpyxl

workbook = openpyxl.Workbook()

sheet = workbook.active

sheet['A1'] = 'Hello World'

print(sheet['A1'].value)