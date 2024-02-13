import openpyxl
workbook = openpyxl.load_workbook('example.xlsx')

sheet = workbook['Sheet1']

print(tuple(sheet['A1':'C3'])) # we slice a part of the worksheet between A1 and C3

for row_of_cell_objects in sheet['A1':'C3']:
    for cell_object in row_of_cell_objects:
        print(cell_object.coordinate, cell_object.value)
    print('---END OF ROW---')


print(list(sheet.columns)[1]) #get second columns shells

for cell_object in list(sheet.columns)[1]: # once converted to sa list indexing as usual
    print(cell_object.value)