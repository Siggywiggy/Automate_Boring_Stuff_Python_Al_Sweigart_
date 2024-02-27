import subprocess
import time

# count down from 60
# pause 1 second between every number in the countdown

for i in range(1, 61):
    print(i)
    time.sleep(1)

# call subprocess.Popen() to open the sound file with the default application
subprocess.Popen(["start", "alarm.wav"], shell=True)
