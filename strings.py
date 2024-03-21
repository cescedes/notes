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

# find() index in a string
god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find('disown')

# including variables into strings with format()
def poem_title_card(title, poet):
  return "The poem \"{}\" is written by {}.".format(title, poet)

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

my_beard_description = poem_description(author = "Shel Silverstein",
title = "My Beard",
original_work = "Where the Sidewalk Ends",
publishing_date = "1974")

#######################################

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print(highlighted_poems)

# split the string into separate items
highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list)

# strip from whitespace each item on the list
highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
print(highlighted_poems_stripped)

# break up all the information for each poem into it’s own list, 
# so we end up with a list of lists.
highlighted_poems_details = []
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))
print(highlighted_poems_details)

# separate out all of the titles, the poets, and the publication dates into their own lists
titles = []
poets = []
dates = []
for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])

# a for loop that uses .format() to print out the following string for each poem: The poem TITLE was published by POET in DATE.
for i in range(len(titles)):
  print("The poem {} was published by {} in {}.".format(titles[i], poets[i], dates[i]))
  i+=1
