import re

# You can use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of the searched text.

# you can put a dollar sign ($) at the end of the regex to indicate the string must end with this regex pattern

begins_with_hello = re.compile(r"^Hello")
print(begins_with_hello.search("Hello, world!"))
print(begins_with_hello.search("He said hello.") == None)

# r'\d$' - mathces strings that end with a digit

ends_with_number = re.compile(r"\d+$")
print(ends_with_number.search("Your number is 42"))
print(ends_with_number.search("Your number is forty two."))

# r'^\d+$ - matches strings that both begin and end with one or more numeric characters

whole_string_is_num = re.compile(r"^\d+$")
print(whole_string_is_num.search("1234567890"))
print(whole_string_is_num.search("12345xyz67890") == None)
print(whole_string_is_num.search("12  34567890") == None)
