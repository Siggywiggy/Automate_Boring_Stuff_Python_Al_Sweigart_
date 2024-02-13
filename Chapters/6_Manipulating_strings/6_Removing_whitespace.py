spam = '    Hello, World    '
print(spam.strip())
print(spam.rstrip())
print(spam.lstrip())

#optional string argument, which characters on the ends should be stripped

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))