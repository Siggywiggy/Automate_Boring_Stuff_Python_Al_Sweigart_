# at least 8 characters long {8,}
# contains both upper and lowercase characters
# at least one digit \d+

import re

# check if password is at least 8 characters long
password_regex = re.compile(r".{8,}")
match_object_1 = password_regex.search("passworD1")
print(match_object_1.group())

# check if at least one digit
# password_regex_2 = re.compile(r'\d+')
# match_object_2 = password_regex_2.search('pasSword1')
# print(match_object_2.group())

# check if password contains both uppercase and lowercase
password_regex_3 = re.compile(r"[a-z]+[A-Z]+\d+")
match_object_3 = password_regex_3.search("passworD4")
print(match_object_3.group() != None)
print(match_object_3.group())
