import re

""" 
function that takes a string and does the same thing as the strip() string method.
If no other arguments are passed other than the string to strip,
then whitespace characters will be removed f
rom the beginning and end of the string. 
Otherwise, the characters specified in the second argument to the function will be removed from the string.
"""


# whitespace_regex = re.compile(r"^(\s)+(.*)(\s)+$")
# match_object_1 = whitespace_regex.search("   Adam Kurm   ")
# print(match_object_1.group(2))


def stripper_function(
    input_string,
    argument=None,
):
    if argument == None:
        whitespace_regex = re.compile(r"^\s*(.*?)\s*$")
        match_object_1 = whitespace_regex.search(str(input_string))

        return match_object_1.groups()

    else:
        strip_regex = re.compile(rf"^{argument}*(.*?){argument}*$")
        match_object_2 = strip_regex.search(str(input_string))

        return match_object_2.groups()


print(stripper_function("   Aadam Kurm   "))
print(stripper_function("llllElise Eritlllll", "l"))
