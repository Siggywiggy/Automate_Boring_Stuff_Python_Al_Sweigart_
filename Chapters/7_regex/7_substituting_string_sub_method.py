import re

# The sub() method for Regex objects is passed two arguments.
# The first argument is a string to replace any matches. The second is the string for the regular expression.
# The sub() method returns a string with the substitutions applied.

names_regex = re.compile(r"Agent \w+")
subbed_string = names_regex.sub(
    "CENSORED", "Agent Alice gave the secret documents to Agent Bob."
)
print(subbed_string)

# In the first argument to sub(), you can type \1, \2, \3, and so on,
# to mean “Enter the text of group 1, 2, 3, and so on, in the substitution.”

agent_names_regex = re.compile(r"Agent (\w)\w+")
subbed_string = agent_names_regex.sub(
    r"\1****",
    "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.",
)
print(subbed_string)
