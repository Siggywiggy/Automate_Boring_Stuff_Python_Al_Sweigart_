import PyPDF2
minutes_file = open('meetingminutes.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(minutes_file)

page = pdf_reader.getPage(0)
page.rotateClockwise(90)

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page)

resulting_pdf_file = open('rotatedPDF.pdf', 'wb')
pdf_writer.write(resulting_pdf_file)
resulting_pdf_file.close()
minutes_file.close()