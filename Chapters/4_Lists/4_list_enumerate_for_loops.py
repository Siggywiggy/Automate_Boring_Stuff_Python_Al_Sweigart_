# on each iteration of loop, enumerate() will return index and item 
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is ' + item)