import openpyxl

workbook = openpyxl.Workbook()

sheet = workbook.active

sheet['A1'] = 'Tall row'

sheet['B2'] = 'Wide column'

# Set the height and width:

sheet.row_dimensions[1].height = 70 # row nr 1 height
sheet.column_dimensions['B'].width = 20 # column B width

workbook.save('dimensions.xlsx')