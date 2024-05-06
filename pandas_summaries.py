import pandas as pd
movies = pd.read_csv('movies.csv')
# Print the first 5 rows 
print(movies.head())

# Print the summary statistics for all columns
print(movies.describe(include='all'))

# Save the mean to mean_budget
mean_budget = movies.production_budget.mean()
print(mean_budget)

# Save the median to med_budget
med_budget = movies.production_budget.median()
print(med_budget)

# Save the mode to mode_budget
mode_budget = movies.production_budget.mode()
print(mode_budget)

# Save the trimmed mean to trmean_budget
from scipy.stats import trim_mean
trmean_budget = trim_mean(movies.production_budget, proportiontocut=0.2)  
print(trmean_budget)

# Save the range to range_budget
range_budget = movies.production_budget.max() - movies.production_budget.min()
print(range_budget)

# Save the interquartile range to iqr_budget
iqr_budget = movies.production_budget.quantile(0.75) - movies.production_budget.quantile(0.25)
print(iqr_budget)
#alternatively
from scipy.stats import iqr
iqr(movies.production_budget)

# Save the variance to var_budget
var_budget = movies.production_budget.var()
print(var_budget)

# Save the standard deviation to std_budget
std_budget = movies.production_budget.std()
print(std_budget)

# Save the mean absolute deviation to mad_budget
mad_budget = movies.production_budget.mad()

######################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
movies = pd.read_csv('movies.csv')

# Create a boxplot for movie budget 
sns.boxplot(x='production_budget', data=movies)
plt.show()
plt.close()

# Create a histogram for movie budget
sns.histplot(x='production_budget', data=movies)
plt.show()
plt.close()

# Save the counts to genre_counts
genre_counts = movies.genre.value_counts()

# Save the proportions to genre_props
genre_props = movies.genre.value_counts() / len(movies.genre)

# Create a bar chart for movie genre 
sns.countplot(x='genre', data=movies)
plt.show()
plt.close()

# Create a pie chart for movie genre
movies.genre.value_counts().plot.pie()
plt.show()
plt.close()
