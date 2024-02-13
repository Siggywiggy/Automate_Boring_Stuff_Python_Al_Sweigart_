import PyPDF2

minutes_file = open('meetingminutes.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(minutes_file)

minutes_first_page = pdf_reader.getPage(0)
pdf_watermark_reader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
minutes_first_page.mergePage(pdf_watermark_reader.getPage(0))

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(minutes_first_page)

#adding all other pages besides the first one
for pageNum in range(1, pdf_reader.numPages):
    page_object = pdf_reader.getPage(pageNum)
    pdf_writer.addPage(page_object)

result_pdf_file = open('watermarked_cover.pdf', 'wb')
pdf_writer.write(result_pdf_file)
minutes_file.close()
result_pdf_file.close()
