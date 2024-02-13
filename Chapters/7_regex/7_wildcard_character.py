import re

# The . (or dot) character in a regular expression is called a wildcard
# and will match any character except for a newline.
# the dot character will match just one character

at_regex = re.compile(r".at")
print(at_regex.findall("The cat in the hat sat on the flat mat."))

at_regex = re.compile(r"..at")
print(at_regex.findall("The cat in the hat sat on the flat mat."))
