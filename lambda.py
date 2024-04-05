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

#return double of the integer if it is bigger than 10, else 0
double_or_zero = lambda num: num*2 if num > 10 else 0
print(double_or_zero(15)) #30
print(double_or_zero(5))  #0
