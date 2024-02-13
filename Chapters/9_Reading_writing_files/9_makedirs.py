import os
from pathlib import Path

print(Path.cwd())

os.makedirs("./testdirectory/")

os.chdir("./testdirectory/")

print(Path.cwd())
