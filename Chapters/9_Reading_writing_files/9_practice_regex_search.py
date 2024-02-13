#! python 3
# a program that opens all .txt files in a folder
# and searches for any line that matches a user-supplied regular expression.
# The results should be printed to the screen.

import pyinputplus as pyip
from pathlib import Path
import re
import sys

while True:
    # take input of folder address
    folder_path = pyip.inputStr(
        prompt="Enter absolute folder path you wish to search in, 'cwd' for current working directory or 'x' to exit: \n"
    )

    if folder_path == "cwd":
        folder_path = Path.cwd()
    elif folder_path == "x":
        sys.exit("Exiting the program!")
    elif Path(folder_path).is_dir():
        folder_path = Path(folder_path)
        break
    else:
        print("No such folder exists!")
        continue


# use glob pattern to match all .txt files in directory, results in glob object!
text_files_in_folder = folder_path.glob("*.txt")

# take input of regex expression that user wants to search for
regex_input = pyip.inputStr(prompt="Enter the regex pattern you wish to search for: \n")

# compile a regex from user input
regex_pattern = re.compile(regex_input, re.I)


for text_file in list(
    text_files_in_folder
):  # loop trough all files one by one filename
    content = open(text_file, "r")  # open the file with the filename
    for line in content:
        if re.findall(regex_pattern, line):
            print("Found a line with a matching regex! \n")
            print(line)
    content.close()
