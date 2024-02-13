#! python 3

# progtam that reads in text files and lets the user add their own text
# anywhere the word ADJECTIVE, NOUN, ADVERB or VERB
# appears in the text file

import pyinputplus as pyip
import re

word_regex = re.compile(r"ADJECTIVE|NOUN|ADVERB|VERB", re.I)

input_file = open("input.txt", "r")
content = input_file.read()
input_file.close()


for found_word in word_regex.findall(
    content
):  # for every found match of the regex pattern
    replacement_word = pyip.inputStr(
        prompt=f"Enter a {found_word.lower()}:"
    )  # take user input
    content = word_regex.sub(replacement_word, content, 1)  # substitute

output_file = open("output.txt", "a")
output_file.write(content)
output_file.close()
