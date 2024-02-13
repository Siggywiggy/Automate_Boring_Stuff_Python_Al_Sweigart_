import re

# | character matches the first occurrence of text

hero_regex = re.compile(r"Batman|Tina Fey")

match_object_1 = hero_regex.search("Batman and Tina Fey")
print(match_object_1.group())

match_object_2 = hero_regex.search("Tina Fey and Batman")
print(match_object_2.group())

# matching one of several patterns as part of my regex

bat_regex = re.compile(r"Bat(man|mobile|copter|bat)")
match_object = bat_regex.search("Batmobile lost a wheel")
print(match_object.group())

print(match_object.group(1))
