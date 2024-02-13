# combining the re.IGNORECASE, re.DOTALL, and re.VERBOSE variables
# using the pipe character (|), which in this context is known as the bitwise or operator.

someRegexValue = re.compile("foo", re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile("foo", re.IGNORECASE | re.DOTALL | re.VERBOSE)
