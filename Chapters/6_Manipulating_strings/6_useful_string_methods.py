spam = "Hello, world!"
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)

print("How are you?")
feeling = input()
if feeling.lower() == "great":
    print("I feel great too.")
else:
    print("I hope the rest of your day is good.")

# The isupper() and islower() methods will return a Boolean True value
# if the string has at least one letter and all the letters are uppercase or lowercase,
# respectively. Otherwise, the method returns False.

spam = "Hello, world!"
print(spam.islower())
print(spam.isupper())
print("HELLO".isupper())
print("abc12345".islower())
print("12345".islower())
print("12345".isupper())
