import shutil, os
from pathlib import Path

home_path = Path.home()
project_path = Path(
    "Documents/Programmeerimine/Automate_boring_stuff_Python/new_run/10_Organizing_files"
)
print(home_path)
print(home_path / project_path)

shutil.copy(
    home_path / project_path / "spam.txt", home_path / project_path / "some_folder"
)

# shutil.copy() returns the path of the newly copied file
print(
    shutil.copy(
        home_path / project_path / "spam.txt", home_path / project_path / "some_folder"
    )
)

# shutil copytree copies every file and subfolder contained, returns a string of the path to the copied folder

shutil.copytree(
    home_path / project_path / "some_folder",
    home_path / project_path / "some_folder_backup",
)
