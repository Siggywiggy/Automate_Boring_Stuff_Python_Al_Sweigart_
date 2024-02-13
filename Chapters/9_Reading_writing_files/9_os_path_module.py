# os.path.abspath(path) will return a string of the absolute path of the argument.

# os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path.

# os.path.relpath(path, start) will return a string of a relative path from the start path to path.
# If start is not provided, the current working directory is used as the start path.

import os
from pathlib import Path

# move up one folder

print(os.path.abspath("."))

os.chdir("..")

# get absolute path of current folder
print(os.path.abspath("."))

# get absolute path of a folder in current folder
print(os.path.abspath("./7_regex/"))


# just a . is not an absolute path
print(os.path.isabs("."))

# get absolute path of current folder (.) with abspath method and then check if its an absolute path with (isabs())
print(os.path.isabs(os.path.abspath(".")))

# relative paths
print(f"current working directory is {Path.cwd()}")

# finds a relative path from current directory to the directory its pointed at

print(
    os.path.relpath("/home/aadamkurm/Documents/Programmeerimine/Python projects/Sudoku")
)
