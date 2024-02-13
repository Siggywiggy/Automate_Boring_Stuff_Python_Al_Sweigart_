#! python3
# program that finds all files with the given prefix, such as spam001.txt, spam002.txt
# in a single folder and locates gaps in numbering
# regardless of gap size will close the gap in numbering of filenames

import re, os, shutil
import pyinputplus as pyip
from pathlib import Path

# get user input

input_prefix = pyip.inputStr(
    prompt="Please input a string to use as a prefix in a filename search: \n"
)


search_folder = str(
    pyip.inputStr(
        prompt="Enter the folder to search or leave blank for current working directory: \n",
        blank=True,
    )
    or Path.cwd()
)

# create a folder to copy in to

os.mkdir(Path(search_folder) / "copied_numberfixed_files")
target_folder = Path(search_folder) / "copied_numberfixed_files"

# regex pattern to match numbered files
file_regex = re.compile(rf"({input_prefix})(0*)(\d*)(.*?)(.txt)")

print(
    f"Currently searching in {search_folder} for files starting with {input_prefix}! \n"
)

# getting all .txt files from the search folder path and sorting them numerically
files = sorted(list(Path(search_folder).glob(f"*.txt")))

# setting up variables to keep track of previous and current numbers

previous_number = 1
current_number = int()

for file_name in files:
    # searching file name for a match with the regex pattern
    match_object = file_regex.search(str(file_name))
    # get the file name parts as a list
    file_name_parts = list(match_object.groups())
    # get the current number in the filename from group(3)
    current_number = int(match_object.group(3))
    # calculate the gaop between prev and curr number
    gap_size = current_number - previous_number
    # if the gap is larger then 1 - eg betwen 3 and 5 gap is 2
    if gap_size > 1:
        new_number = current_number - gap_size + 1
        file_name_parts[2] = str(new_number)
        # adding a prefix 00 to the new number - keep it consistent
        file_name_parts[1] = "00"

        new_file_name = Path(target_folder) / "".join(file_name_parts)
        # copying the current file name to a new location with new filename
        shutil.copy(file_name, new_file_name)
        # setting previous number to new number to keep the gap correct going forward in the loop
        previous_number = new_number

    else:
        # if no gap in numbers just copy the file over to the new location
        shutil.copy(file_name, target_folder / os.path.basename(file_name))
        previous_number = current_number

finished_files = list(Path(target_folder).glob(f"*.txt"))

print("New filenames are: \n")
for filename in finished_files:
    print(filename)
