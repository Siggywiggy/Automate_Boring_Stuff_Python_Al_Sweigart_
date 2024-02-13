# shutil.move(source, destination) will move a file or folder and returns
# absolute path of the new location
# if cant find destination folder will rename the file or folder in to the destination!
import shutil, os
from pathlib import Path

home_path = Path.home()
project_path = Path(
    "Documents/Programmeerimine/Automate_boring_stuff_Python/new_run/10_Organizing_files"
)

shutil.move(
    home_path / project_path / "spam.txt",
    home_path / project_path / "some_folder_backup" / "spam_backup_2.txt",
)
