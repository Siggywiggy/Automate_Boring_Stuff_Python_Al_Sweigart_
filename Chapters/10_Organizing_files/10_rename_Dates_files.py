#! Python3
# files with American-style dates (MM-DD-YYYY)
# renamed to European-style dates (DD-MM-YYYY)
import shutil
import os
import re


# create regex that can identify text pattern of american style dates

date_pattern = re.compile(
    r"""
^(.*?) 				# all text before the date
((0|1)?\d)- 		# one or two digits for the month
((0|1|2|3)?\d)- 	# one or two digits for the day
((19|20)\d\d)   	# four digits for the year
(.*?)$ 				# all text after the date
""",
    re.VERBOSE,
)


# call os.listdir() to find all the files in working directory

# loop over each filename, use regex to check whether it has an american style date

for american_file_name in os.listdir("."):
    match_object = date_pattern.search(american_file_name)
    # skip files without a dat
    if match_object == None:
        continue

    # get the different parts of the filename
    before_part = match_object.group(1)
    month_part = match_object.group(2)
    day_part = match_object.group(4)
    year_part = match_object.group(6)
    after_part = match_object.group(8)

    month_part, day_part = day_part, month_part

    euro_file_name = (
        before_part + "-" + day_part + "-" + month_part + "-" + year_part + after_part
    )
    abs_working_directory = os.path.abspath(".")
    american_file_name = os.path.join(abs_working_directory, american_file_name)
    euro_file_name = os.path.join(abs_working_directory, euro_file_name)
    # if it has the date, rename the file with shutil.move()
    # shutil.move(src, dst, copy_function=copy2)
    print(f"Renaming {american_file_name} to {euro_file_name}...")
    shutil.move(american_file_name, new_file_name)
