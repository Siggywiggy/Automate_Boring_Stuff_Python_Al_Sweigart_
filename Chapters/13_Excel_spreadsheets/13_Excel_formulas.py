import openpyxl
workbook = openpyxl.Workbook()

sheet = workbook.active

sheet['A1'] = 200
sheet['A2'] = 300
sheet['A3'] = '=SUM(A1:A2)' # Set the formula.
workbook.save('writeFormula.xlsx')