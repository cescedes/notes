#a function called password_generator() that takes two inputs, first_name and last_name, 
# and then concatenates the last three letters of each and returns them as a string.
def password_generator(first_name, last_name):
  password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return password
temp_password = password_generator("Reiko", "Matsuki")

# a function called contains that takes two arguments, big_string and little_string
# and returns True if big_string contains little_string.
# For example contains("watermelon", "melon") should return True
# contains("watermelon", "berry") should return False.
def contains(big_string, little_string):
  return little_string in big_string

# a function called common_letters that takes two arguments, string_one and string_two
# and then returns a list with all of the letters they have in common.
def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

# username_generator takes two inputs, first_name and last_name and returns a user_name.
# The username should be a slice of the first three letters of their first name and the first four letters of their last name.
# If their first name is less than three letters or their last name is less than four letters it should use their entire names.
# For example, if the employee’s name is Abe Simpson the function should generate the username AbeSimp.
def username_generator(first_name, last_name):
  username = first_name[:3] + last_name[:4]
  return username

# password_generator function to take the input user_name and
# shift all of the letters by one to the right, so the last letter of the username
# ends up as the first letter and so forth.
# For example, if the username is AbeSimp, then the temporary password generated should be pAbeSim.
def password_generator(user_name):
  password = ''
  for i in range(len(user_name)):
    password += user_name[i-1]
  return password
print(password_generator("apple"))

# authors as a one big string
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
author_names = authors.split(',')
print(author_names)

# a list called author_last_names that only contains
# the last names of the poets in the provided string.
author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
print(author_last_names)

# love_maybe poem lines
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

# used .strip() on each line in the list to remove the unnecessary whitespace and save it as a new list love_maybe_lines_stripped.
love_maybe_lines_stripped = []
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())

#.join() the lines in love_maybe_lines_stripped together into one large multi-line string, love_maybe_full, that can be printed to display the poem.
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)

# fix name in string with replace() method
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')


