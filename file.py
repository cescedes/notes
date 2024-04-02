# read file
with open('welcome.txt') as text_file:
  text_data = text_file.read()
print(text_data)

# print line by line
with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)

# single line
with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
print(first_line)

# write file
with open('bad_bands.txt', 'w') as bad_bands_doc:
  bad_bands_doc.write('BTS')
  
# append to file
with open('cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write("Air Buddy\n")

# read csv file
with open('logger.csv') as log_csv_file:
  data = log_csv_file.read()
print(data)

# open csv file and convert that data into a dictionary using the csv library’s DictReader object.
# We pass the additional keyword argument newline='' to the file opening open() function
# so that we don’t accidentally mistake a line break in one of our data fields as a new row in our CSV
import csv
with open('cool_csv.csv', newline='') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  # The keys of the dictionary are, by default, the entries in the first line of our CSV file.
  # For each row in cool_csv_dict print out that row’s "Cool Fact".
  for row in cool_csv_dict:
    print(row['Cool Fact'])

# Create a list called isbn_list, iterate through books_reader
# to get the ISBN number of every book in the CSV file.
import csv
isbn_list = []
with open('books.csv', newline='') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter = '@')
  for row in books_reader:
    isbn_list.append(row['ISBN'])

# writing a csv file
# First we want the headers, so we call .writeheader() on the writer object. 
# This writes all the fields passed to fieldnames as the first row in our file.
# Then we iterate through our big_list of data.
# Each item in big_list is a dictionary with each field in fields as the keys. 
# We call output_writer.writerow() with the item dictionaries which writes each line to the CSV file.
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv
with open('logger.csv', 'w') as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)

  log_writer.writeheader()
  for item in access_log:
    log_writer.writerow(item)

# reading json file
import json
with open('message.json') as message_json:
  message = json.load(message_json)
print(message['text'])

# writing json file
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json
with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)
