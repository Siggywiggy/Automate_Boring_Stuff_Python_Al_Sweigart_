import csv

# if the files contain header rows its easier to work with Dict-Reader/Writer objects
# using dictionaries to write and read - first row of csv file are keys of the dictionary

example_file = open('exampleWithHeader.csv')
example_dict_reader = csv.DictReader(example_file)

for row in example_dict_reader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])

example_file.close()

# if there are no column headers in the first row, its possible to supply header as second argument

example_file = open('example.csv')
example_dict_reader = csv.DictReader(example_file, ['time', 'name', 'amount'])

print('inserted header row tags')
for row in example_dict_reader:
    print(row['time'], row['name'], row['amount'])

example_file.close()

# DictWriter objects

output_file = open('output.csv', 'w', newline='')
output_DictWriter = csv.DictWriter(output_file, ['Name', 'Pet', 'Phone'])
output_DictWriter.writeheader()
output_DictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
output_DictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'}) # if no key:value pair the corresponding column will be empty
output_DictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})
output_file.close()
