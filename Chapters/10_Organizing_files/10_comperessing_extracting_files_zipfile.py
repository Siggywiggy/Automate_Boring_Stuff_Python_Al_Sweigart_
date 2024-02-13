import zipfile
import os
from pathlib import Path

zip_path = Path(
    "/home/aadamkurm/Documents/Programmeerimine/Automate_boring_stuff_Python/new_run/10_Organizing_files/"
)
example_zip = zipfile.ZipFile(zip_path / "example.zip")
print(example_zip.namelist())

spam_info = example_zip.getinfo("spam.txt")
print(spam_info.file_size)
print(spam_info.compress_size)
print(
    f"Compressed file is {round(spam_info.file_size / spam_info.compress_size, 2)}x smaller!"
)

example_zip.extractall(zip_path / "extracted_examplezip")
example_zip.extract("spam.txt")
example_zip.close()
