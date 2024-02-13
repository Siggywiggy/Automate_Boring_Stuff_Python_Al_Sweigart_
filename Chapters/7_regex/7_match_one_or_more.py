import re

"""
The + (or plus) means “match one or more.”
The group preceding a plus must appear at least once.

Match ONE or MULTIPLE

"""

bat_regex = re.compile(r'Bat(wo)+man')

# Example 1

match_object_1 = bat_regex.search('The Adventures of Batwoman')
print(match_object_1.group())

# Example 2

match_object_2 = bat_regex.search('The Adventures of Batwowowowowowowowoman')
print(match_object_2.group())

# Example 3 - no occurrance, will return None
match_object_3 = bat_regex.search('The Adventures of Batman')
print(match_object_3 == None)