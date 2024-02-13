import pyinputplus as pyip

response = pyip.inputNum("Enter num: ")  # doe not allow blank entry

response = pyip.inputNum("Enter number or leave blank: ", blank=True)  # allows blank entries, input is optional
