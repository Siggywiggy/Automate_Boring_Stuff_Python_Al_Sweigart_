import os, shutil
from pathlib import Path
import pyinputplus as pyip

# get file extension input, block invalid symbols from file extension with blockRegexes
file_extension = "." + pyip.inputStr(
    prompt="Please input extension you would like to search for:... ",
    blockRegexes=[r"[<>:\"/\|?]"],
)

search_folder = str(
    pyip.inputStr(
        prompt="Enter the folder to search or leave blank for current working directory",
        blank=True,
    )
    or Path.cwd()
)

target_folder = Path(search_folder) / "copied_files"

# creating the target folder

os.mkdir(target_folder)

print(
    f"Looking for {file_extension} files in {search_folder} and copying to {target_folder}"
)

# walking trough all folders in search folder

for foldername, subfolders, filenames in os.walk(search_folder):
    # create an iterator from a glob pattern matching search extension
    for file_name in Path(foldername).glob(f"*{file_extension}"):
        file_name_target = os.path.split(file_name)[-1]

        # create target file path
        target_file_path = Path(target_folder / file_name_target)

        # determine if a file with the same name is already copied or not
        for foldername_target, subfolders_target, filenames_target in os.walk(
            target_folder
        ):
            if file_name_target in filenames_target:
                print(f"{file_name_target} already copied, skipping!")
                continue
            else:
                shutil.copy(file_name, target_file_path)
