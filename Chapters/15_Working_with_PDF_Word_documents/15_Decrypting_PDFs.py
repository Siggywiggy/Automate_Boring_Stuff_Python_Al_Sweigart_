import PyPDF2
#pdf_reader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
#print(pdf_reader.isEncrypted)
#print(pdf_reader.getPage(0))

pdf_reader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdf_reader.decrypt('rosebud') # decrypt only decrypts PdfFileReader object
page_object = pdf_reader.getPage(0)
print(page_object.extractText())
pdf_reader.close()