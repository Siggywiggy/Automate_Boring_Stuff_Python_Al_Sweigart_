from pathlib import Path
import os

# absolute path, which always begins with the root folder
# relative path, which is relative to the program’s current working directory

# . - this directory
# .. - parent directory

# is_absolute if path represents an absolute path returns TRUE

current_path = Path.cwd()
print(current_path)
print(current_path.is_absolute())

# getting absolute path from relative path

relative_path = Path("/Automate_boring_stuff_Python/new_run/")

os.chdir("/home/aadamkurm/Documents/Programmeerimine/")
print(Path.cwd())

absolute_path = Path.cwd() / relative_path

print(absolute_path)

# get absolute path using the home directory

relative_path = Path(
    "/aadamkurm/Documents/Programmeerimine/Automate_boring_stuff_Python/new_run/"
)

print(Path.home() / relative_path)
