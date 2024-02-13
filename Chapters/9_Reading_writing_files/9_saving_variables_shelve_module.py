import shelve

# shelve open needs a file path as a string, cant accept Path?
shelf_file = shelve.open("my_data")
cats = ["Zophie", "Pooka", "Simon"]
shelf_file["cats"] = cats
shelf_file.close()

shelf_file = shelve.open("my_data")

# print(type(shelf_file))

# prints the keys in shelve file
print(list(shelf_file.keys()))

# prints values in shelve file
print(list(shelf_file.values()))

# can access values by keys
print(shelf_file["cats"])


shelf_file.close()
