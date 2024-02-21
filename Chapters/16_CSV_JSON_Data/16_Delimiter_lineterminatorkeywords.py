import csv

csv_file = open('example.tsv', 'w', newline='')
csv_writer = csv.writer(csv_file, delimiter='\t', lineterminator='\n\n') #delimiter tab and double space between lines

csv_writer.writerow(['apples', 'oranges', 'grapes'])
csv_writer.writerow(['eggs', 'bacon', 'ham'])
csv_writer.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])

csv_file.close()