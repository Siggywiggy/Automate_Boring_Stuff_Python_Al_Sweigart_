import openpyxl
workbook = openpyxl.Workbook()

sheet = workbook.active

for i in range (1, 11):
    sheet['A' + str(i)] = i

reference_object = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1,
max_row=10)

series_object = openpyxl.chart.Series(reference_object, title='First series')

chart_object = openpyxl.chart.BarChart()
chart_object.title = 'My Chart'
chart_object.append(series_object)
sheet.add_chart(chart_object, 'C5')
workbook.save('sample_chart.xlsx')