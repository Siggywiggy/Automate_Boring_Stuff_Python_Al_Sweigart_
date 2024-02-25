#! python 3
# track the time elapsed between presses of ENTER
# print lap number, total time and lap time
import time

print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')


input() # press ENTER to begin
print('Started.')

time_start = time.time()
last_time = time_start

lap_counter = 1

# start tracking the lap times
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - time_start, 2)
        print(f'Lap {lap_counter} : {total_time} ({lap_time})')
        lap_counter += 1
        last_time = time.time()

except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')