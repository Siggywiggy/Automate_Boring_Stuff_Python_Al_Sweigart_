import pprint

cats = [{"name": "Zophie", "desc": "chubby"}, {"name": "Pooka", "desc": "fluffy"}]

print(pprint.pformat(cats))

file_obj = open("my_cats.py", "w")

file_obj.write("cats = " + pprint.pformat(cats) + "\n")

file_obj.close()

import my_cats

print(my_cats.cats)
print(my_cats.cats[0])
print(my_cats.cats[1])
