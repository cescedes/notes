#Simulating Randomness
import numpy as np
import pandas as pd

monthly_report = pd.read_csv('monthly_report.csv')

#simulate one visitor:
# who has a 10% chance of making a purchase (p=0.1).
one_visitor = np.random.choice(['y', 'n'], size=1, p=[0.1, 0.9])
print(one_visitor)
#simulate 500 visitors:
simulated_monthly_visitors=np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])
print(simulated_monthly_visitors)

##
#The first step in running a hypothesis test is to form a null hypothesis.
#Simulating the Null Distribution

null_outcomes = []
#run an experiment where we simulate a sample of 500 visitors, each with a 10% chance of making a purchase,10000 times
for i in range(10000): 
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])
  num_purchased = np.sum(simulated_monthly_visitors == 'y')
  null_outcomes.append(num_purchased)

#calculate the minimum and maximum values in null_outcomes here:

null_min=np.min(null_outcomes)
null_max=np.max(null_outcomes)
print(null_min)
print(null_max)

#plot the histogram here:
plt.hist(null_outcomes)
plt.axvline(41, color = 'r') #In the month we’re investigating, we calculated that there were 41 purchases. Add a vertical line to your histogram at 41.
plt.show()

##
#Confidence Intervals
#calculate the 90% interval here:
null_90CI = np.percentile(null_outcomes, [5,95])
#np.percentile(outcomes, [2.5,97.5]) #95% interval 

##
#Calculating a One-Sided P-Value
#estimate the p-value for a binomial hypothesis test with the following null and alternative hypotheses:

#Null: the probability of a purchase was 10%
#Alternative: the probability of a purchase rate was LESS THAN 10%
#In other words, calculate the proportion of values in null_outcomes that are less than or equal to 41 (the observed number of purchases that we calculated earlier)
#calculate the p-value here:
null_outcomes = np.array(null_outcomes)
p_value = np.sum(null_outcomes <= 41)/len(null_outcomes) 
print(p_value) 

##
#Calculating a Two-Sided P-Value
#calculate the p-value for a two-sided test (alternative hypothesis is that the purchase probability was DIFFERENT FROM 10%). 
#Remember that, if the purchase rate is 10%, we expect 50 of the 500 visitors to make a purchase.
#in other words, calculate the proportion of values in null_outcomes that are less than or equal to 41 (the number of purchases we observed in our sample, which is 9 fewer than 50) 
#OR greater than or equal to 59 (which is 9 purchases more than 50). 
#calculate the p-value here:
null_outcomes = np.array(null_outcomes)
p_value = np.sum((null_outcomes <= 41) | (null_outcomes >= 59))/len(null_outcomes)
print(p_value) 

#####
#Writing a Binomial Test Function
from scipy.stats import binom_test

def simulation_binomial_test(observed_successes, n, p):
  #initialize null_outcomes
  null_outcomes = []
  
  #generate the simulated null distribution
  for i in range(10000):
    simulated_monthly_visitors = np.random.choice(['y', 'n'], size=n, p=[p, 1-p])
    num_purchased = np.sum(simulated_monthly_visitors == 'y')
    null_outcomes.append(num_purchased)

  #calculate a 1-sided p-value
  null_outcomes = np.array(null_outcomes)
  p_value = np.sum(null_outcomes <= observed_successes)/len(null_outcomes) 
  
  #return the p-value
  return p_value

#Test your function below by uncommenting the code below. the simulation function gives you a very similar answer to the binom_test function from scipy:
p_value1 = simulation_binomial_test(45, 500, .1)
print("simulation p-value: ", p_value1)

p_value2 = binom_test(45, 500, .1, alternative = 'less')
print("binom_test p-value: ", p_value2)
#Output:
#simulation p-value:  0.2548
#binom_test p-value:  0.25468926056232155

#Binomial Testing with SciPy
from scipy.stats import binom_test

# A two-sided test for whether the observed 41 purchases among 500 visitors is far enough from the expected 10% purchase rate to convince you that the purchase rate was different from expectation this week
p_value_2sided = binom_test(41, n=500, p=0.1)
print(p_value_2sided)
# a one-sided test where the alternative hypothesis is that the probability of a visitor making a purchase was less than 10% (0.1)
p_value_1sided = binom_test(41, n=500, p=0.1,alternative = 'less')
print(p_value_1sided)

