import threading
import time

print('Start of program.')

def take_a_nap():
    time.sleep(5)
    print('Wake up!')

thread_object = threading.Thread(target = take_a_nap)
thread_object.start()

print('End of program!')