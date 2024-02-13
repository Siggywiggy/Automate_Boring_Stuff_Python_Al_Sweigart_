# if word starts with vowel "yay" is appended
# if word starts with consonant or consonant cluster (ch or gr) then
# the consonant cluster is moved to the end + appended ay

# English to pig lain

print('Enter the English message to translate into Pig Latin:')
message = input()

vowels = ('a', 'e', 'i', 'o', 'u', 'y')

pig_latin = []

for word in message.split():
    #separate the non-letters at the start of this word
    prefix_non_letters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]
    
    if len(word) == 0:
        pig_latin.append(prefix_non_letters)
        continue

    # separate the non-letters at the end of this word

    suffix_non_letters = ''
    while not word[-1].isalpha():
        suffix_non_letters = word[-1] + suffix_non_letters
        word = word[:-1]

    # remember if the word was in Uppercase or Title Case
    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower() # make word lowercase for translation

    #separate consonants at the start of this word:
    prefix_consonants = ''
    while len(word) > 0 and not word[0] in vowels:
        prefix_consonants += word[0]
        word = word[1:]

    #add pig latin ending to the word
    if prefix_consonants != '':
        word += prefix_consonants + 'ay'
    else:
        word += 'yay'
    
    # set word word back to uppercase or title case

    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()
    
    # add non-letters back to the start or the end of the word.
    pig_latin.append(prefix_non_letters + word + suffix_non_letters)


# Join all the words back together into a single string

print(' '.join(pig_latin))