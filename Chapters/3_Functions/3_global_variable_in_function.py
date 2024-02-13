def spam():
    global eggs #accessing global variable from local function scope
    eggs = 'spam'

eggs = 'global'
spam() #replacing the content of eggs variable with value 'spam'
print(eggs)

#######################

def spam():
    global eggs
    eggs = 'spam' #this is the global

def bacon():
    eggs = 'bacon' #this is a local variable

def ham():
    print(eggs) #this is a global variable because there is no variable not global statement

eggs = 42 # this is the global
spam()
print(eggs)
ham()