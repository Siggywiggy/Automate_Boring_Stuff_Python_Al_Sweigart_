import pathlib
import subprocess
from pathlib import Path


python_exe = Path(
    "C:\\Users\\Aadam\\Automate_Boring_Stuff_Python_Al_Sweigart_\\Chapters\\venv\\Scripts\\python.exe"
)
subprocess_file = Path(
    "C:\\Users\\Aadam\\Automate_Boring_Stuff_Python_Al_Sweigart_\\Chapters\\17_Time_Scheduling_tasks_launching_programs\\hello.txt"
)
subprocess.Popen([python_exe, subprocess_file])
