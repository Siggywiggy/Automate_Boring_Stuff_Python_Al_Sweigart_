import re

# verbose modew can be enabled by passing the variable re.VERBOSE as the second argument to re.compile()

phone_regex = re.compile(
    r"""(
	(\d{3}|\(\d{3}\))? 	# area code - 3 x digits PIPE/OR (3x digits) - optional ? 
	(\s|-|\.)? 			# separator space/newline PIPE followed by - PIPE followed by .
	\d{3} 				# first 3 digits
	(\s|-|\.) 			# separator space/newline PIPE followed by - PIPE followed by .
	\d{4}				# last 4 digits
	(\s*(ext|x|ext.)\s*\d{2,5})? # extension - space once or more, ext PIPE ext PIPE x match everything, space once or more, digits 2 to 5
	)""",
    re.VERBOSE,
)
