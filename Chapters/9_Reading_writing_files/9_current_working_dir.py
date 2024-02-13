# cwd

from pathlib import Path
import os

# print current working directory

print(Path.cwd())

# change directtory

os.chdir("/home/aadamkurm/Downloads/")

# print current working directory

print(Path.cwd())

# print your home directory

print(Path.home())
