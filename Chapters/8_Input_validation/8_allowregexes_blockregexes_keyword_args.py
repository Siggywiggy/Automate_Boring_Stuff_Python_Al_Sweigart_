# allowRegexes and blockRegexes keyword arguments take a list
# of regular expression strings to determine what
# the PyInputPlus function will accept or reject as valid input

import pyinputplus as pyip

# allows uppercase roman numerals

response = pyip.inputNum(allowRegexes=[r"(I|V|X|L|C|D|M)+", r"zero"])

print(response)

# allows lowercase roman numerals

response = pyip.inputNum(allowRegexes=[r"(i|v|x|l|c|d|m)+", r"zero"])
print(response)

# blockregexes - function wont accept these

response = pyip.inputNum("Please input a non-even number: ", blockRegexes=[r"[02468]$"])
print(response)

# If you specify both an allowRegexes and blockRegexes argument,
# the allow list overrides the block list.

# allows only caterpillar and category, blocks everything else containing cat

response = pyip.inputStr(
    allowRegexes=[r"caterpillar", "category"], blockRegexes=[r"cat"]
)
print(response)
