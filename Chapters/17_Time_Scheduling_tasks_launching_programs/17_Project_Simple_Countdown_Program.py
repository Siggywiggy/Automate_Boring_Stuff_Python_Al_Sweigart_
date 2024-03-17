import subprocess
import time

# count down from 60
# pause 1 second between every number in the countdown

for i in range(1, 5):
    print(i)
    time.sleep(1)

# call subprocess.Popen() to open the sound file with the default application
subprocess.Popen(["xdg-open alarm.wav"], shell=True)
