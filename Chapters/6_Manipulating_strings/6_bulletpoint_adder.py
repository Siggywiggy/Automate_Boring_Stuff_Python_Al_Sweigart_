#!
# bulletpoint_adder.py - ads Wikipedia bullet points to the start
# of each line fo text on the clipboard

import pyperclip

text = pyperclip.paste()

#separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
    

text = '\n'.join(lines)

print('Successfully added bulletpoints to your list!')
pyperclip.copy(text)
