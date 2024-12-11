import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

population = pd.read_csv("salmon_population.csv")
population = np.array(population.Salmon_Weight)
pop_mean = round(np.mean(population),3)

## Plotting the Population Distribution
sns.histplot(population, stat='density')
plt.axvline(pop_mean,color='r',linestyle='dashed')
plt.title(f"Population Mean: {pop_mean}")
plt.xlabel("Weight (lbs)")
plt.show()
plt.clf() 

samp_size = 30
# Generate our random sample below
sample = np.random.choice(np.array(population), samp_size, replace = False)

### Define sample mean below
sample_mean = round(np.mean(sample), 3)

sns.histplot(sample, stat='density')
plt.axvline(sample_mean,color='r',linestyle='dashed')
plt.title(F"Sample Mean: {sample_mean}")
plt.xlabel("Weight (lbs)")
plt.show()

# smaller sample sizes will have sample means that vary more from each other each time you take a random sample.
# With a small sample, extreme values can significantly impact the sample mean, causing it to vary from one sample to the next.

#Let’s estimate the sampling distribution of the mean using a population of cod fish.
#We’ve set the sample size equal to 50 and created a for loop to take 500 random samples.

population = pd.read_csv("cod_population.csv")
# Save transaction times to a separate numpy array
population = population['Cod_Weight']

sample_size = 50
sample_means = []

for i in range(500):
  samp = np.random.choice(population, sample_size, replace = False)
  # calculate mean here
  this_sample_mean = np.mean(samp)
  # append here
  sample_means.append(this_sample_mean)

sns.histplot(sample_means,stat='density')
plt.title("Sampling Distribution of the Mean")
plt.xlabel("Weight (lbs)")
plt.show()

########

cod_population = pd.read_csv("cod_population.csv")
# Save transaction times to a separate numpy array
population = cod_population['Cod_Weight']

sns.histplot(population, stat = 'density' )
plt.title("Population Distribution")
plt.show()

sample_means = []

# Below is our sample size
samp_size = 50

for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    this_sample_mean = np.mean(samp)
    sample_means.append(this_sample_mean)

plt.clf() # this closes the previous plot
sns.histplot(sample_means, stat = 'density' )
plt.title("Sampling Distribution of the Mean")
plt.xlabel("Weight (lbs)")
plt.show()

## when increased the sample size, the sampling distribution look more normal.

###
# when the original population is normally distributed, the CLT applies even with a smaller sample size.
###
###### Calculating Probabilities #######
## Setting up our parameters
std_dev = 20
samp_size = 25
standard_error = std_dev / (samp_size**.5)
# we can use the normal CDF to calculate the probability that a sample of 25 fish has a mean weight of 30 lbs.
x=750/25 # Because we want 25 fish to weigh less than 750 lbs, we want our sample mean to be 750/25, or 30 lbs.
mean = 36
cod_cdf = stats.norm.cdf(x, mean, standard_error)
#The probability of 25 fish having an average weight of 30 or less is 10%. Based on this, it’s probably a good idea to put less fish in the crate or to get a sturdier crate.

###

#In order to review, let’s consider an example from a restaurant serving quarter-pounder burgers. Their quarter-pounders weigh an average of 0.25 lbs with a standard deviation of 0.2 lbs.

#Let’s say we weigh all their burgers that they cook for dinner on a given night. 64 people order quarter-pounders. What is the probability that the mean will be 0.24 lbs or less?
# 0.345
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Set up parameters here:
x = 0.24
population_mean = 0.25
population_std_dev = 0.2
samp_size = 64

### Below is code to create simulated dataset and calculate Standard Error
standard_error = population_std_dev / (samp_size**.5)

this_cdf = round(stats.norm.cdf(x,population_mean,standard_error),3)

# Create the population
population = np.random.normal(population_mean, population_std_dev, size = 100000)

# Simulate the sampling distribution
sample_means = []
for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    sample_means.append(np.mean(samp))

mean_sampling_distribution = round(np.mean(sample_means),3)
std_sampling_distribution = round(np.std(sample_means),3)

std_error = population_std_dev / (samp_size **0.5)

sns.histplot(population, stat = 'density')
plt.title(f"Population Mean: {population_mean} \n Population Std Dev: {population_std_dev} \n Standard Error = {population_std_dev} / sq rt({samp_size}) \n Standard Error = {std_error} ")
plt.xlabel("")
plt.show()
plt.clf()

# Plot the sampling distribution
sns.histplot(sample_means, stat = 'density')
plt.axvline(x,color='r',linestyle='dashed')
plt.title(f"Sampling Dist Mean: {mean_sampling_distribution} \n Sampling Dist Standard Deviation: {std_sampling_distribution}\n CDF for x={x}: {this_cdf}")
plt.xlabel("")
plt.show()
