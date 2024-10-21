## Random Variables ##

import numpy as np
# create 6 sided "die"
die_6 = range(1, 7)
# set number of rolls
num_rolls = 10
# roll the "die" the set amount of times
results_1 = np.random.choice(die_6, size = num_rolls, replace = True)
# create 12-sided "die"
die_12 = range(1, 13)
# roll the 12-sided "die" 10 times
results_2 = np.random.choice(die_12, size = num_rolls, replace = True)

## CALCULATING PROBABILITY ##
## probability mass function ##

import scipy.stats as stats
# value of interest
x = 3
# sample size
n = 10
# calculate probability of observing 3 heads in 10 fair coin flips.
prob_1 = stats.binom.pmf(x, n, 0.5)
########
import scipy.stats as stats
# the probability of observing between 4 to 6 heads from 10 coin flips
prob_1 = stats.binom.pmf(4, n = 10, p = 0.5) + stats.binom.pmf(5, n = 10, p = 0.5) + stats.binom.pmf(6, n = 10, p = 0.5) 
# observing more than 2 heads from 10 coin flips
prob_2 = 1 - (stats.binom.pmf(0, n = 10, p = 0.5) + stats.binom.pmf(1, n = 10, p = 0.5) + stats.binom.pmf(2, n = 10, p = 0.5))

## cumulative distribution function ## 

import scipy.stats as stats
# observing 3 or fewer heads from 10 fair coin flips
prob_1 = stats.binom.cdf(3, 10, 0.5)
# compare to pmf code 
print(stats.binom.pmf(0, n=10, p=.5) + stats.binom.pmf(1, n=10, p=.5) + stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5))

# observing more than 5 heads from 10 fair coin flips
prob_2 = 1 - stats.binom.cdf(5, 10, 0.5)
# observing between 2 and 5 heads from 10 fair coin flips
prob_3 = stats.binom.cdf(5, 10, 0.5) - (stats.binom.cdf(1, 10, 0.5))
# compare to pmf code
print(stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5) + stats.binom.pmf(5, n=10, p=.5))

## probability density function ## 

import scipy.stats as stats
#x: the value of interest
#loc: the mean of the probability distribution
#scale: the standard deviation of the probability distribution
# stats.norm.cdf(x, loc, scale)
prob = stats.norm.cdf(175, 167.64, 8)

# The weather in the Galapagos islands follows a Normal distribution with a mean of 20 degrees Celcius and a standard deviation of 3 degrees.
# the probability that the weather on a randomly selected day will be between 18 to 25 degrees Celcius using the norm.cdf() method
temp_prob_1 = stats.norm.cdf(25, 20, 3) - stats.norm.cdf(18, 20, 3)

# the probability that the weather on a randomly selected day will be greater than 24 degrees Celsius
temp_prob_2 = 1 - (stats.norm.cdf(24, 20, 3))

################################################################################

## REVIEW ##

import scipy.stats as stats
import numpy as np

## Exercise 1
# sampling from a 6-sided die
die_6 = range(1, 7)
print(np.random.choice(die_6, size = 5, replace = True))

## Exercise 4 - binomial probability mass function
# 6 heads from 10 fair coin flips
print(stats.binom.pmf(6, 10, 0.5))

## Exercise 6 - binomial probability mass function
# 2 to 4 heads from 10 coin flips
# P(X = 2) + P(X = 3) + P(X = 4)
print(stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5))

# 0 to 8 heads from 10 coin flips
# 1 - (P(X = 9) + P(X = 10))
print(1 - (stats.binom.pmf(9, n=10, p=.5) + stats.binom.pmf(10, n=10, p=.5)))

## Exercise 9 - binomial cumulative distribution function
# 6 or fewer heads from 10 coin flips
print(stats.binom.cdf(6, 10, 0.5))

# more than 6 heads from 10 coin flips
print(1 - stats.binom.cdf(6, 10, 0.5))

# between 4 and 8 heads from 10 coin flips
print(stats.binom.cdf(8, 10, 0.5) - stats.binom.cdf(3, 10, 0.5))

## Exercise 10 - normal distribution cumulative distribution function
# stats.norm.cdf(x, loc, scale)
# temperature being less than 14*C
  # x = 14, loc = 20, scale = 3
print(stats.norm.cdf(14, 20, 3))

# Exercise 11
# temperature being greater than 24*C
  # x = 24, loc = 20, scale = 3
print(1 - stats.norm.cdf(24, 20, 3))

# temperature being between 21*C and 25*C
  # x = 24, loc = 20, scale = 3
print(stats.norm.cdf(25, 20, 3) - stats.norm.cdf(21, 20, 3))


############################################

# POISSON DIST 

# PMF

#the average number of calls in our call center between 9am and 10am to be 15 calls.
#What is the probability that we would see exactly 15 calls in that time frame?
prob_15 = stats.poisson.pmf(15, 15) 
# the probability we would get between 7 and 9 calls, the average is 15
prob_7_to_9 = stats.poisson.pmf(9, 15) + stats.poisson.pmf(8, 15) + stats.poisson.pmf(7, 15)

# CDF

# what is the probability of observing more than 20 calls?
prob_more_than_20 = 1 - stats.poisson.cdf(20, 15)
# the probability of observing between 17 to 21 calls when the expected number of calls is 15
prob_17_to_21 = stats.poisson.cdf(21, 15) - stats.poisson.cdf(16, 15)

# generate random poisson sample
from histogram_function import histogram_function
# lambda = 15, 1000 random draws 
rand_vars = stats.poisson.rvs(15, size = 1000)
rvs.mean(rand_vars)
#histogram_function() takes a list of random variables and plots them to a histogram
histogram_function(rand_vars)

########################################

import scipy.stats as stats

## You work at ambulance dispatch where the number of calls that come in daily follows the Poisson distribution with lambda equal to 9. 
#There’s a rule that a team can go on no more than 12 calls a day. But how often could this happen?
calls = 1 - stats.poisson.cdf(12, 9)

## Let’s say that you have to call in a backup team if you have 10 or more calls in a given day. 
#But you don’t want to have to call in a backup team unless they really will be needed.
#But what is the probability that they will be called and not needed?
false_backup = stats.poisson.cdf(12, 9) - stats.poisson.cdf(9, 9)

## A certain tennis star has a first-serve rate of 62%. Let’s say they serve 80 times in a given match.
#What is the expected value of the number of serves they make?
expected_serves = 80*0.62

## At the same first-serve rate, what is the variance of this player’s first-serves?
variance_serves = 80*0.62*(1-0.62)


