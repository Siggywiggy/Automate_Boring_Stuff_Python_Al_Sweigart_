import datetime
import time

print(datetime.datetime.now())

date_time_object = datetime.datetime(2024, 2, 25, 22,35, 37)
print(date_time_object.year)
print(date_time_object.month)
print(date_time_object.day)
print(date_time_object.hour)
print(date_time_object.minute)
print(date_time_object.second)

# converting unix epoch timestamp
converted_unix_epoch = datetime.datetime.fromtimestamp(1000000)
print(converted_unix_epoch)

converted_current_time = datetime.datetime.fromtimestamp(time.time())
print(converted_current_time)

halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
print(halloween2019 == oct31_2019)
print(halloween2019 > newyears2020)
print(newyears2020 > halloween2019)
print(newyears2020 != oct31_2019)