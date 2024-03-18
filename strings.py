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
