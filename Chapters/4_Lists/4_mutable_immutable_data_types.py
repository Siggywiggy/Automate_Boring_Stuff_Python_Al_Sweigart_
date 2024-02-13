#strings are immutable

name = 'Zophie a cat'
new_name = name[0:7] + 'the' + name[8:12]

print(name)
print(new_name)

#lists are mutable

#replacing existing list value with brand new list value
eggs = [1, 2, 3]
print(eggs)
eggs = [4, 5, 6]
print(eggs)

# modifying original list 
eggs = [1, 2, 3]
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append(4)
eggs.append(5)
eggs.append(6)
print(eggs)