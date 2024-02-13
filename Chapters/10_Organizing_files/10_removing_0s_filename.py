#! python3
# remove zeros in front of digits in filenames


import shutil
import os
import re

# create regex

zero_pattern = re.compile(
    r"""
	^(.*?) 		# all text before zeros
	(0+) 		# one or more zeros
	(\d+) 		# one or more digits
	(.*?)$ 		# all text after digits
	""",
    re.VERBOSE,
)

current_working_dir = os.getcwd()

# loop over filenames returned by os.listdir() method

for filename in os.listdir(current_working_dir):
    match_object = zero_pattern.search(filename)
    if match_object == None:
        continue
    print(filename)
    print(match_object.groups())
    before_part = match_object.group(1)
    digits_part = match_object.group(3)
    after_part = match_object.group(4)

    new_file_name = before_part + digits_part + after_part

    # get absolute path of current working directory
    abs_working_directory = os.path.abspath(".")
    # create path string for old filename
    old_file_name = os.path.join(abs_working_directory, filename)
    # create path string for new filename
    new_file_name = os.path.join(abs_working_directory, new_file_name)
    # move the file rewriting its name
    shutil.move(old_file_name, new_file_name)
