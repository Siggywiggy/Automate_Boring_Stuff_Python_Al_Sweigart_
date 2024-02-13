import os
import shutil

# os.unlink(path) will delete the file at path
# os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
# shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.

from pathlib import Path

# permanently deletes so it would be wise to run with print command first

for filename in Path.home().glob("*.rxt"):
    # os.unlink(filename)
    print(filename)

# removing a file and a folder
home_path = Path.home()
project_path = Path(
    "Documents/Programmeerimine/Automate_boring_stuff_Python/new_run/10_Organizing_files"
)

if os.path.isfile(home_path / project_path / "spam.txt"):
    s.unlink(home_path / project_path / "spam.txt")

if os.path.isdir(home_path / project_path / "some_folder"):
    shutil.rmtree(home_path / project_path / "some_folder")

if os.path.exists(home_path / project_path / "some_folder_backup"):
    shutil.rmtree(home_path / project_path / "some_folder_backup")
