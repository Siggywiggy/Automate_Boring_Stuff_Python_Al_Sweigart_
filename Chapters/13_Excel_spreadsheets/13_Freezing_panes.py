import openpyxl
workbook = openpyxl.load_workbook('produceSales.xlsx')
sheet = workbook.active
sheet.freeze_panes = 'A2' # Freeze the rows above A2.
workbook.save('freeze_panes_example.xlsx')