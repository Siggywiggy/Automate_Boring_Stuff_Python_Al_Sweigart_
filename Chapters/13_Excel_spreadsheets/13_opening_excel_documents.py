import openpyxl
workbook = openpyxl.load_workbook('example.xlsx')
print(type(workbook))