import re

# the dot character means “any single character except the newline,”
# and the star character means “zero or more of the preceding character.”

# GREEDY MODE

name_regex = re.compile(r"First Name: (.*) Last Name: (.*)")
match_object = name_regex.search("First Name: Al Last Name: Sweigart")
first_name, last_name = match_object.groups()

print(first_name, last_name)

# NON GREEDY MODE - ?

non_greedy_regex = re.compile(r"<.*?>")
match_object = non_greedy_regex.search("<To serve man> for dinner.>")
print(match_object.group())

greedy_regex = re.compile(r"<.*>")
match_object = greedy_regex.search("<To serve man> for dinner.>")
print(match_object.group())
