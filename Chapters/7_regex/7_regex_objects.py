# \d - digit character 0-9
# \d\d\d-\d\d\d-\d\d\d\d

# multiplication with {x}
# \d{3}-\d{3}-\d{4}

import re

# Passing a string value representing your regular expression to re.compile()
# returns a Regex pattern object (or simply, a Regex object).
phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
match_object = phone_num_regex.search("My number is 415-555-4242.")
print("Phone number found: " + match_object.group())

# parentheses create GROUPS within the match object - 1, 2, 3 etc

phone_num_regex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
match_object = phone_num_regex.search("My number is 415-555-4242.")
# area code is group 1
print(match_object.group(1))
# phone number is group 2
print(match_object.group(2))
# index 0 or none returns the whole matching text
print(match_object.group(0))
print(match_object.group())

# .groups() method retrieves all groups at once, multiple assignment

area_code, main_number = match_object.groups()
print(area_code)
print(main_number)

# escape character \ lets you match a special regex character in text like () or ^ etc
phone_num_regex = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
match_object = phone_num_regex.search("My phone number is (415) 555-4242.")
print(match_object.group(1))
print(match_object.group(2))
