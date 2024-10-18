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


