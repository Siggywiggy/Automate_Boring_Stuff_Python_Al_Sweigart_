import re

""" 
# \\d - digits from 0 to 9
# \\D - any character that is NOT a numeric digit from 0 to 9
# \\w - any letter, numeric digit or underscore letter (word characters)
# \\W - any numeric character that is NOT a letter, numeric digit or underscore character
# \\s - any space, newline or tab character (space characters)
# \\S - any character that not NOT a space, tab or newline 
# [a-zA-Z] character class will only match upper and lowercase letters

"""

[0 - 5] == (0 | 1 | 2 | 3 | 4 | 5)

xmas_regex = re.compile(
    r"\d+\s\w+"
)  # digits one or more, any space/newline/tab, any letter one or more

findall_result = xmas_regex.findall(
    "12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge"
)

print(findall_result)
