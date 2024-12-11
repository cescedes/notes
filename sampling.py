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
