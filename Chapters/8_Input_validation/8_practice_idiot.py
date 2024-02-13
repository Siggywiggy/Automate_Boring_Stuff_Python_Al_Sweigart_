import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?'
    response = pyip.inputYesNo(prompt, yesVal = 'yes', noVal = 'no')
    if response == 'no':
        break
    else:
        continue


print('Thank you! Have a nice day.')