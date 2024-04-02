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
#W e pass the additional keyword argument newline='' to the file opening open() function
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

