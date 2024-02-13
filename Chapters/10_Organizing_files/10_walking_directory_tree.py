import os
from pathlib import Path

for folder_name, sub_folders, file_names in os.walk(
    Path.home() / "Documents/IoT_projects/Arduino"
):
    print(f"The current folder is {folder_name}")
    for sub_folder in sub_folders:
        print(f"subfolders are inside {folder_name} : {sub_folder}")
    for file_name in file_names:
        print(f"File inside {folder_name} : {file_name}")
