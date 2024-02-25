import datetime

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days)
print(delta.seconds)
print(delta.microseconds)
print(delta.total_seconds())

print(str(delta))

# adding and substracting with datetime objects or other timedelta objects

oct_21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
about_30_years = datetime.timedelta(days=365 * 30)
print(oct_21st)
print(oct_21st - about_30_years)
print(oct_21st - (2 * about_30_years))