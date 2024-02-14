import PyPDF2
import os
from pathlib import Path
import logging

# comment out to enable logging
#logging.disable(logging.CRITICAL)

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s -  %(levelname) s -  %(message)s"
)

logging.debug("Start of program")

# find all PDF files in cwd
path = Path(os.getcwd())
logging.debug(print(f'current working dir is {path}.'))
list_of_PDF_files = list(path.glob("*.pdf"))
# sort the list of filenames alphabetically
list_of_PDF_files.sort()
logging.debug(print(list_of_PDF_files))
# create PdfFileWriter object for the output PDF
pdf_writer = PyPDF2.PdfFileWriter()
# get the cover page from the very first PDF file and insert it in pdf_writer
logging.debug(f'the first file is {list_of_PDF_files[0]}')
cover_page_file = open(os.path.basename(list_of_PDF_files[0]), 'rb')
pdf_reader = PyPDF2.PdfFileReader(cover_page_file)
cover_page = pdf_reader.getPage(0)
pdf_writer.addPage(cover_page)

# loop over every PDF file and create PdfFileReader object
for filename in list_of_PDF_files:
    open_file = open(filename, 'rb')
    try:
        pdf_reader = PyPDF2.PdfFileReader(open_file)
        logging.debug(f'The filename is {os.path.basename(filename)} and the file is {pdf_reader.numPages} pages long')
        # loop over every page except first page
        for page_num in range(1, pdf_reader.numPages):
            page_object = pdf_reader.getPage(page_num)
            # add pages to output PDF PdfFileWriter object
            pdf_writer.addPage(page_object)

    except PyPDF2.utils.PdfReadError as err:
        print(f'something went wrong with opening the file {os.path.basename(filename)}: {err}')
        continue


result_pdf = open('all_minutes.pdf', 'wb')

pdf_writer.write(result_pdf)

result_pdf.close()
