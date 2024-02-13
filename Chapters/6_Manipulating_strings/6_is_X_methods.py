# isalpha() Returns True if the string consists only of letters and isn’t blank
print("hello".isalpha())

# isalnum() Returns True if the string consists only of letters and numbers and is not blank
print("hello123".isalnum())
print("hello".isalnum())

# isdecimal() Returns True if the string consists only of numeric characters and is not blank
print("123".isdecimal())

# isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank
print("    ".isspace())

# istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters
print("This Is Title Case".istitle())
print("This Is Title Case 123".istitle())
print("This Is not Title Case".istitle())
print("This Is NOT Title Case Either".istitle())

while True:
    print("Enter your age:")
    age = input()
    if age.isdecimal():
        break
    print("Please enter a number for your age.")

while True:
    print("Select a new password (letters and numbers only):")
    password = input()
    if password.isalnum():
        break
    print("Passwords can only have letters and numbers.")
