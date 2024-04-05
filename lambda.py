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

#take num, return even or odd
even_or_odd = lambda num: "even" if num%2==0 else "odd"
print(even_or_odd(10))  #even
print(even_or_odd(5))   #odd

#multiple of three
multiple_of_three = lambda num: "multiple of three" if num%3==0 else "not a multiple"
print(multiple_of_three(9))
print(multiple_of_three(10))

#rate movie
rate_movie = lambda rating: "I liked this movie" if rating > 8.5 else "This movie was not very good"
print(rate_movie(9.2))
print(rate_movie(7.2))

#ones_place that returns the ones’ place of the input num. #the rightmost position of a number
ones_place = lambda num: num%10
print(ones_place(123))
print(ones_place(4))

#return twice the square of num
double_square = lambda num: 2*(num**2)
print(double_square(5))
print(double_square(3))

#return num plus a random integer number between 1 and 10 (inclusive)
import random
add_random = lambda num: num + random.randint(1,10)
print(add_random(5))
print(add_random(100))
