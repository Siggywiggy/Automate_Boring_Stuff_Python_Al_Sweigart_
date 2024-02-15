import csv

example_file = open('example.csv')

example_reader = csv.reader(example_file)

for row in example_reader:
    print(f'row {example_reader.line_num} + {row}')

# THE READER OBJECT CAN ONLY BE LOOPED OVER ONCE
