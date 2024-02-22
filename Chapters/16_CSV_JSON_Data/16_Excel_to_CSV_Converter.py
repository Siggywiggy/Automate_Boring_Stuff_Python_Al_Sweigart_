import csv
import sys
import openpyxl
import os
import logging
from pathlib import Path

# comment out to enable logging
#logging.disable(logging.CRITICAL)

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s -  %(levelname) s -  %(message)s"
)

logging.debug("Start of program")

starting_folder = Path.cwd() / 'excelSpreadsheets'
logging.debug(f'the starting location is {starting_folder}')

file_names = list(starting_folder.glob("*.xlsx"))
# loop trough every file matching the glob pattern in folder
for file_name in file_names:
    logging.debug(f'file name is {file_name}')
    workbook = openpyxl.load_workbook(file_name, 'rb')
    workbook_sheetnames = workbook.sheetnames
    # loop trough every sheet in the workbook
    for sheet_name in workbook_sheetnames:
        logging.debug(f'sheet name is {sheet_name}')
        # create the CSV filename from Excel filename and sheet title
        csv_filename = starting_folder / (os.path.basename(file_name).split('.')[0] + '_' + sheet_name + '.csv')
        logging.debug(f'new csv file name is {csv_filename}')
        # Create the csv.writer object for this CSV file.
        output_file = open(csv_filename, 'w',newline='')
        output_writer_object = csv.writer(output_file)
        # loop trough every row in the sheet
        for row_num in range(1, workbook[sheet_name].max_row +1):
            row_data = list()
            
            for col_num in range(1, workbook[sheet_name].max_column +1):
                row_data.append(workbook[sheet_name].cell(row=row_num, column=col_num).value)
		
            output_writer_object.writerow(row_data)
	
            #print(row_data)
        output_file.close()
