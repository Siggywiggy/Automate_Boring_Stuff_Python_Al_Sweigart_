import pyinputplus as pyip

response = pyip.inputNum(
    "Please enter a number:"
)  # will return int or float instead of str

response_2 = pyip.inputInt("Please enter an integrer:")

# min, max, greaterThan, and lessThan keyword arguments
response_3 = pyip.inputNum("Enter number >= 4: ", min=4)
response_4 = pyip.inputNum("Enter number > 4: ", greaterThan=4)
response_5 = pyip.inputNum("Enter 4 >= number < 6", min=4, lessThan=6)
