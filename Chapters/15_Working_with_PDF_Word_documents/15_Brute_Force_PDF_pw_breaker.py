import PyPDF2

pdf_reader = PyPDF2.PdfFileReader(open('combinedminutes_encrypted.pdf', 'rb'))
dict_file = open('dictionary.txt', 'r')

password_list = list()

for word in dict_file.readlines():
    password_list.append(word.rstrip('\n'))

#print(password_list)

for password in password_list:
    if pdf_reader.decrypt(password.upper()) == 1:
        print(f'The password is {password.upper()}')
        break
    elif pdf_reader.decrypt(password.lower()) == 1:
        print(f'The password is {password.lower()}')
        break
    else:
        continue