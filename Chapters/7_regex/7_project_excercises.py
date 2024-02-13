import re

# finds both https and http urls

url_regex = re.compile(r"(http://|https://)(.*)")
match_object = url_regex.search("https://automatetheboringstuff.com/2e/chapter7/")
print(match_object.group())
print(match_object.groups())

# cleaning up dates

date_regex = re.compile(r"(\d{1,4})(/|.|-)(\d{1,4})(/|.|-)(\d{1,4})")
date_example = "such as 3/14/2019, 03-14-2019, and 2015/3/19"
match_object_2 = date_regex.findall(date_example)
print(match_object_2)


# find common typos

# multiple spaces
# (\s+) # more then one space[('', '', ' '), ('', '', 'accidentally '), ('', '!!', ''), ('', '', 'of '), ('', '', 'are '), ('', '!!', '')]

# (\w*\s)+ #zero or more characters followed by space repeated
# ([!]+)Find common typos such as multiple spaces between words, accidentally accidentally repeated words, or multiple exclamation marks at the end of sentences. Those are annoying!!
typos_regex = re.compile(r"(\s{2,})|([!]+)")
typos_example_text = """Find common typos such as multiple  spaces between   words, accidentally accidentally repeated!! words, or multiple exclamation marks at the end of of sentences. Those are annoying!!"""
match_object_3 = typos_regex.findall(typos_example_text)
print(match_object_3)

# question 18 If numRegex = re.compile(r'\d+'), 
# what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

num_regex = re.compile(r'\d+')
print(num_regex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens'))

# question 20 - How would you write a regex that matches
# a number with commas for every three digits?
comma_regex = re.compile(r'^\d{1,3}(,\d{3})*$') 
match_object = comma_regex.search('6,368,745')
print(match_object.group())

# question 21 - write a regex that matches the full name of someone whose last name is Watanabe

name_regex = re.compile(r'[A-Z][a-zA-Z]+\s[A-Z][a-zA-Z]+')
match_object = name_regex.search('RoboCop Watanabe')
print(match_object)

# question 22
# the first word is either Alice, Bob, or Carol;
# the second word is either eats, pets, or throws;
# the third word is apples, cats, or baseballs; 
# and the sentence ends with a period
# case-insensitive
sentence_regex = re.compile(r'^(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)
match_object = sentence_regex.search('Carol throws baseballs.')
print(match_object)

