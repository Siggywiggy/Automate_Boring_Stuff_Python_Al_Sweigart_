import csv

example_file = open('example.csv')

example_reader_object = csv.reader(example_file)

example_data = list(example_reader_object)

print(example_data)
print(example_data[0][0])
print(example_data[2][2])