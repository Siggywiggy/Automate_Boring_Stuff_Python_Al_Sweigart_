from pathlib import Path
import os

p = Path("C:/Users/Al/spam.txt")

# root folder of the filesystem
print(p.anchor)

# folder that contains the file, evaluates to a Path object!
print(p.parent)

# name of the file - stem + suffi
print(p.name)

# stem
print(p.stem)

# suffix
print(p.suffix)

# no drive for MacOS and Linux
print(p.drive)

# parent Path object

print(Path.cwd())

print(Path.cwd().parents[0])

print(Path.cwd().parents[1])


# OS module dirname(path) and basename(path)

calcFilePath = "/home/aadamkurm/Documents/Programmeerimine/Automate_boring_stuff_Python/new_run/9_Reading_writing_files/9_parts_of_file_path.py"

# basename returns everything after the last /
print(os.path.basename(calcFilePath))

# dirname returns everything before last /
print(os.path.dirname(calcFilePath))

# getting a tuple of dir name and base name together use a split() method
print(os.path.split(calcFilePath))

# same result with basename and dirname methods
print((os.path.dirname(calcFilePath), os.path.basename(calcFilePath)))

# getting a lost of folder names from a path
print(calcFilePath.split(os.sep))
