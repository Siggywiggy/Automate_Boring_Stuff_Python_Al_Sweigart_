# first argument is key to check for and second argument is the value to set if the key does not exist
# if the key exists setdefault() returns the keys value

spam = {"name": "Pooka", "age": 5}
spam.setdefault("color", "black")
print(spam.items())

# color key already exists, so will return the keys value
print(spam.setdefault("color", "white"))
