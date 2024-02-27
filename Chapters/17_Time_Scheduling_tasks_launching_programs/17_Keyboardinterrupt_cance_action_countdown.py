import time
import subprocess

countdown_length = 10
print("Press Control + C to cancel opening Paint")

try:
    for i in range(countdown_length + 1):
        print(i)
        time.sleep(1)

    paint_process = subprocess.Popen(
        "C:\\Users\\Aadam\\AppData\\Local\\Microsoft\\WindowsApps\\mspaint.exe"
    )

except KeyboardInterrupt:
    print("Canceling opening Paint!")
