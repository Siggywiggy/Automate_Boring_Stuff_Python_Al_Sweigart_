#! python3
# a progrom to detect and list all files larger then 100 Megabytes


import os
from pathlib import Path
import pyinputplus as pyip

# get file extension input, block invalid symbols from file extension with blockRegexes

search_folder = str(
    pyip.inputStr(
        prompt="Enter the folder to search or leave blank for current working directory",
        blank=True,
    )
    or Path.cwd()
)

os.chdir(search_folder)

print(Path.cwd())

for folder_name, sub_folders, file_names in os.walk(search_folder):
    # print(folder_name)
    for file_name in file_names:
        if os.path.getsize(Path(folder_name) / file_name) > 100000000:
            print(f"{file_name} larger than 100MB!")
