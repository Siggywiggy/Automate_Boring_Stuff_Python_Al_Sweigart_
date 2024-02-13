# Write a function named collatz() that has one parameter named number.
# If number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.

number = None

while not number:
    try:    
        print('Enter the starting number for Collatz sequence: ')
        number = int(input())
    except ValueError:
        print('You must enter a numeric integer value!')

def collatz(number):
    if number % 2 == 0:
        print(number // 2) 
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


while True:
    number = collatz(number)
    if number == 1:
        break

print(number)