    import pyinputplus as pyip

# series of digits that adds up to 10
# Accepts a single string argument of what the user entered
# Raises an exception if the string fails validation
# Returns None (or has no return statement) if inputCustom() should return the string unchanged
# Returns a non-None value if inputCustom() should return a different string from the one the user entered
# Is passed as the first argument to inputCustom()

def adds_up_to_ten(numbers):
    
    numbers_list = numbers.split(',')
    sum = 0 
    for num in numbers_list:
        sum += int(num)
    
    if sum == 10:
        print(f'The numbers add up correctly to 10 - {sum}')
        return int(sum)
    
    else:
        raise Exception(f'The digits must add up to 10, not {sum}.')
        


print('Please enter a series of digits, that adds up to 10, separated by commas: ')
response = pyip.inputCustom(adds_up_to_ten, blockRegexes=[r'[a-zA-Z]'])