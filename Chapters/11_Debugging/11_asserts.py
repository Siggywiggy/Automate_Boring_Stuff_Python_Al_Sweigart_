# assertions are for programmer errors
# python -o filename.py will run the file with assertions turned off

ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
print(ages)
assert ages[0] <= ages[-1]  # does nothing because returns True

ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.reverse()
print(ages)
assert ages[0] <= ages[-1]  # returns AssertionError because returns False
