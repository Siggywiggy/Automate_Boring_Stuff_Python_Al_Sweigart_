spam = {"color": "red", "age": 42}

for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)

# getting a true list from one of the methods with list() function

print(list(spam.keys()))

# multiple assignment

for k, v in spam.items():
    print("Key: " + k + " Value: " + str(v))
