#! python3
# 7_project_phone_email_extractor.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re


phone_regex = re.compile(
    r"""(
	(\d{1,3}|\(\d{1,3}\))? 	# area code - 3 x digits PIPE/OR (3x digits) - optional ? 
	(\s|-|\.)?  			# separator space OR - OR .
	(\d{3}) 				# first 3 digits
	(\s|-|\.)  			# separator space OR - OR .
	(\d{4}) 				# last 4 digits
	(\s*(ext|x|ext.)\s*\d{2,5})? # optional extension - space once or more, ext PIPE ext PIPE x match everything, space once or more, digits 2 to 5
	)""",
    re.VERBOSE,
)

# email regex

email_regex = re.compile(
    r"""(
	[a-zA-Z0-9._%+-]+      # username
	@                      # @ symbol
	[a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )""",
    re.VERBOSE | re.IGNORECASE,
)

# Find matches in clipboard text

text = str(pyperclip.paste())


matches = []

for groups in phone_regex.findall(text):
    phone_num = "-".join([groups[1], groups[3], groups[5]])
    if groups[6] != "":
        phone_num += " x" + groups[6]
    matches.append(phone_num)

for groups in email_regex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard:")
    print("\n".join(matches))
else:
    print("No phone numbers or email addresses found")
