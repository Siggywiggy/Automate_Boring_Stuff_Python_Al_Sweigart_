import PyPDF2

pdf_file_1 = open('meetingminutes.pdf', 'rb')
pdf_file_2 = open('meetingminutes2.pdf', 'rb')

pdf_reader_1 = PyPDF2.PdfFileReader(pdf_file_1)
pdf_reader_2 = PyPDF2.PdfFileReader(pdf_file_2)

pdf_writer = PyPDF2.PdfFileWriter()

for page_num in range(pdf_reader_1.numPages):
    page_object = pdf_reader_1.getPage(page_num)
    pdf_writer.addPage(page_object)

for page_num in range(pdf_reader_2.numPages):
    page_object = pdf_reader_2.getPage(page_num)
    pdf_writer.addPage(page_object)

pdf_output_file = open('combinedminutes.pdf', 'wb')
pdf_writer.write(pdf_output_file)

pdf_output_file.close()
pdf_file_1.close()
pdf_file_2.close()