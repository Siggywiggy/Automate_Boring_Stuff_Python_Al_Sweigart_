spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)

# reverse keyword

spam.sort(reverse=True)
print(spam)

#.sort() method sorts in place
#cant sort a list of mixed number values and string values

spam = [1, 3, 2, 4, 'Alice', 'Bob']
#spam.sort()

#.sort() ,ethod uses ASIIbetical order
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)


#sorting in regular alphabetical order

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)
