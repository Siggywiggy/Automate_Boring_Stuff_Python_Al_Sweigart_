# is like simplyfied regex patterns

from pathlib import Path
import os

p = Path(
    "/home/aadamkurm/Documents/Programmeerimine/Automate_boring_stuff_Python/new_run/9_Reading_writing_files"
)

# * - any and all files
print(list(p.glob("*")))  # makes a list from the generator

# lists all .py files
print(list(p.glob("*.py")))

# ? - for any single character

print(list(p.glob("?_p*")))

# iterating over generator returned form glob()

p = Path(
    "/home/aadamkurm/Documents/Programmeerimine/Automate_boring_stuff_Python/new_run/9_Reading_writing_files"
)

for python_file in p.glob("?_*.?y"):
    print(python_file)  # prints the path object as a string
