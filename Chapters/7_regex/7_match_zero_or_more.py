import re

"""
The group that precedes the star can occur any number of times in the text.
It can be completely absent or repeated over and over again.

Match ZERO, ONE or MULTIPLE
"""

# Example 1

bat_regex = re.compile(r"Bat(wo)*man")
match_object_1 = bat_regex.search("The Adventures of Batman")

print(match_object_1.group())  # Batman

# Example 2

match_object_2 = bat_regex.search("The Adventures of Batwoman")
print(match_object_2.group())  # Batwoman

# Example 3

match_object_3 = bat_regex.search("The Adventures of Batwowowowowowowowoman")
print(match_object_3.group())  # Batwowowowowowowowoman
