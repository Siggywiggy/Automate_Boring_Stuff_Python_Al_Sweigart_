import re

"""search() will return a Match object of the first matched text in the searched string,
 the findall() method will return the strings of every match in the searched string
"""
phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

mo = phone_num_regex.search("Cell: 415-555-9999 Work: 212-555-0000")

(print(mo.group()))

# findall() will return a list of strings - as long as there are no groyus in the regex

phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")  # has no groups

list_results = phone_num_regex.findall("Cell: 415-555-9999 Work: 212-555-0000")
print(list_results)

# findall() with groups - list of tuples

phone_num_regex = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")  # has groups
tuple_results = phone_num_regex.findall("Cell: 415-555-9999 Work: 212-555-0000")
print(tuple_results)
