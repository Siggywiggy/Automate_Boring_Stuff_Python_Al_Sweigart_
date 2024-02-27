import subprocess

subprocess.Popen("C:\\Windows\\System32\\calc.exe")
# subprocess.Popen('C:\\Program Files\\NewDesignTool\\Program\\NewDesignTool.exe')
# subprocess.Popen('/snap/bin/gnome-calculator')

# poll() method returns None if te process is still running
# poll() method returns processes integer exit code - 0 exited without error

# wait method  - will block the continuation of program until the launched process
# has terminated

paint_process = subprocess.Popen(
    "C:\\Users\\Aadam\\AppData\\Local\\Microsoft\\WindowsApps\\mspaint.exe"
)
# True if the process is still stunning
print(paint_process.poll() == None)
# doesnt return until MS Paint closes
paint_process.wait()
# False if the process has exited
print(paint_process.poll() == None)
