import copy

spam = ['A', 'B', 'C', 'D']
print(id(spam))

#copy creates a separate list with unique ID

cheese = copy.copy(spam)
print(id(cheese))

cheese[1] = 42

print(spam)
print(cheese)

# copy.deepcopy() to copy lists containing lists

spam = [['aadam', 'elise'], 'A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
print(spam)
print(cheese)