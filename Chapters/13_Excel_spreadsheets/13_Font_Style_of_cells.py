import openpyxl
from openpyxl.styles import Font

workbook = openpyxl.Workbook()
sheet = workbook['Sheet']

italic_24_font = Font(size=24, italic=True) # create font

sheet['A1'].font = italic_24_font # apply the font to A1

sheet['A1'] = 'HELLO, World!'

font_object_1 = Font(name='Times New Roman', bold=True, size=16)

sheet['A2'] = 'Bold Times New Roman'

sheet['A2'].font = font_object_1

font_object_2 = Font(size=24, italic=True)

sheet['A3'].font = font_object_2

sheet['A3'] = '24pt Italic'

workbook.save('styles.xlsx')
