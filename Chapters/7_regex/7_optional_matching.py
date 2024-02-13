import re

"""
The regex should find a match regardless of whether that bit of text is there.
The ? character flags the group that precedes it as an optional part of the pattern. 

Match ZERO or ONE!

"""

# Example 1

bat_regex = re.compile(r'Bat(wo)?man')

match_object_1 = bat_regex.search('The Adventures of Batman')
print(match_object_1.group())

match_object_2 = bat_regex.search('The Adventures of Batwoman')
print(match_object_2.group())

# Example 2

phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

match_object_1 = phone_regex.search('My number is 415-555-4242')
print(match_object_1.group())

match_object_2 = phone_regex.search('My number is 555-4242')
print(match_object_2.group())