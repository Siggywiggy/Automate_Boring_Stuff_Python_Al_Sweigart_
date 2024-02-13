# (Ha){3} == 'HaHaHa' but != 'HaHa'
# (Ha){3,5} - range specific
# Ha){3,} - 3 or more instances
# ( Ha){,5} - 0 to 5 instances and no more

import re

ha_regex = re.compile(r"(Ha){3}")
match_object_1 = ha_regex.search("HaHaHa")

print(match_object_1.group())

# will not match

match_object_2 = ha_regex.search("Ha")
print(match_object_2 == None)

# greedy vbs nongreedy

# GREEDY

greedy_haha_regex = re.compile(r"(Ha){3,5}")
match_object_1 = greedy_haha_regex.search("HaHaHaHaHa")
print(match_object_1.group())  # will return the maximum it can - greedy

# NON GREEDY

non_greedy_haha_regex = re.compile(r"(Ha){3,5}?")
match_object_2 = non_greedy_haha_regex.search(r"HaHaHaHaHa")
print(match_object_2.group())  # only matches 3x HaHaH
