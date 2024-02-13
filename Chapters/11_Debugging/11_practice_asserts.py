"""Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10."""

spam = 4
# assert spam > int(10)

"""Write an assert statement that triggers an AssertionError if the variables
eggs and bacon contain strings that are the same as each other, 
even if their cases are different (that is, 
'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).

"""

eggs = "goodbye"
bacon = "GOODbye"

# assert eggs.lower() != bacon.lower()

"""
Write an assert statement that always triggers an AssertionError
"""

assert False != False
