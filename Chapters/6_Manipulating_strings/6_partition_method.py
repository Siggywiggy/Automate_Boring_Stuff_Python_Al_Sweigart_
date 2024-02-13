"""partition() method searches the string it is called on 
for the separator string it is passed, and returns 
a tuple of three substrings for the
 “before,” “separator,” and “after” substrings. 
 Only splits the string on FIRST occurrance"""

#partitioning on 'w'
print('Hello, world!'.partition('w'))

#partitioning on 'world'
print('Hello, world!'.partition('world'))

# if separatior string cant be found, firt string returned in tuple will be 
# entire string and the other two will be empty
print('Hello, world!'.partition('XYZ'))

# multiple assignment
before, sep, after = 'Hello, world!'.partition(' ')
print(before, sep, after)