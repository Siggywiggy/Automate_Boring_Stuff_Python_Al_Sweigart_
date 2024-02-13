import re

# re.DOTALL makes . character match ALL characters including newline character

no_newline_regex = re.compile(".*")
match_object = no_newline_regex.search(
    "Serve the public trust.\nProtect the innocent.\nUphold the law."
)

print(match_object.group())

newline_regex = re.compile(".*", re.DOTALL)
match_object = newline_regex.search(
    "Serve the public trust.\nProtect the innocent.\nUphold the law."
)
print(match_object.group())
