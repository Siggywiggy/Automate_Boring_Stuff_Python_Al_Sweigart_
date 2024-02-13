import random

pets = ['Dog', 'Cat', 'Moose']

print(random.choice(pets))

print('Randomly shuffling a list:')
print(pets)
random.shuffle(pets)
print('The shuffled list:')
print(pets)