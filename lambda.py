#return true if the input contains 'a'
contains_a = lambda word: 'a' in word
print(contains_a("banana")) #True
print(contains_a("apple"))  #True
print(contains_a("cherry")) #False

#return true if the string length > 12
long_string = lambda str: len(str) > 12
print(long_string("short"))   #False
print(long_string("photosynthesis")) #True

#return true if the string ends in 'a'
ends_in_a = lambda str: 'a' in str[-1]
print(ends_in_a("data"))     #True
print(ends_in_a("aardvark")) #False


