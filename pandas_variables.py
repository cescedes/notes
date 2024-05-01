print(movies.dtypes)

#If a variable appears with the wrong data type, we can change it with the .astype() function.
movies['cast_count'] = movies['cast_count'].astype("int64")

#The pandas .Categorical() method can be used to store data as type category and indicate the order of the categories. if we use .sort_values(), the DataFrame will be sorted by the logical order
#Change the data type of the rating variable to categorical. Set an order of [‘NR’, ‘G’ , ‘PG’, ‘PG-13’, ‘R’].
movies['rating'] = pd.Categorical(movies['rating'],['NR', 'G' , 'PG', 'PG-13', 'R'], ordered=True)

#Check the new order of the categories with .unique()
print(movies.rating.unique())

# Create a new dataframe with the `mfr` variable One-Hot Encoded
cereal = pd.get_dummies(data=cereal, columns=['mfr'])

###########################

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas Dataframe
auto = pd.read_csv('autos.csv', index_col=0)

# Print the first 10 rows of the auto dataset
print(auto.head(10))

# Print the data types of the auto dataframe
print(auto.dtypes)

# Change the data type of price to float
auto['price'] = auto['price'].astype('float')

# Set the engine_size data type to category
auto['engine_size'] = pd.Categorical(auto['engine_size'], ['small', 'medium', 'large'], ordered=True)

print(auto['engine_size'].unique())

# Create the engine_codes variable by encoding engine_size
auto['engine_codes'] = auto['engine_size'].cat.codes

print(auto.head())

# One-Hot Encode the body-style variable
auto = pd.get_dummies(auto, columns=['body-style'])

print(auto.head())

#################################

# column	description
# first_name	The respondent’s first name.
# last_name	The respondent’s last name.
# birth_year	The respondent’s year of birth.
# voted	If the respondent participated in the current voting cycle.
# num_children	The number of children the respondent has.
# income_year	The average yearly income the respondent earns.
# higher_tax	The respondent’s answer to the question: “Rate your agreement with the statement: the wealthy should pay higher taxes.”
# marital_status	The respondent’s current marital status.


import codecademylib3

# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

print(census.head())
print(census.dtypes)
print(census['birth_year'].unique())

#There appears to be a missing value in the birth_year column. With some research you find that the respondent’s birth year is 1967.
#Use the .replace() method to replace the missing value with 1967, so that the data type can be changed to int. Then recheck the values in birth_year by calling the .unique() method and printing the results.
census['birth_year'] = census['birth_year'].replace(['missing'], 1967)
print(census['birth_year'].unique())

census['birth_year'] = census['birth_year'].astype(int)
print(census.dtypes)

#print the average birth year of the respondents
print(census['birth_year'].mean())

#set an order to the higher_tax variable so that: strongly disagree < disagree < neutral < agree < strongly agree.
census['higher_tax'] = pd.Categorical(census['higher_tax'], ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'], ordered=True)

#print the new order
print(census['higher_tax'].unique())

#Label encode the higher_tax variable
census['higher_tax'] = census['higher_tax'].cat.codes

#print the median
print(census['higher_tax'].median())

#One-Hot Encode marital_status
census = pd.get_dummies(census,columns=['marital_status'])
print(census.head())

#a new variable called marital_codes by Label Encoding the marital_status variable
census['marital_codes'] = census['marital_status'].cat.codes

#a new variable called age_group, which groups respondents based on their birth year. The groups should be in five-year increments, e.g., 25-30, 31-35, etc.
bins = list(range(census['birth_year'].min(), census['birth_year'].max() + 6, 5))
labels = [f'{i}-{i+4}' for i in bins[:-1]]
census['age_group'] = pd.cut(census['birth_year'], bins=bins, labels=labels, right=False)
print(census[['birth_year', 'age_group']].head())

#label encode the age_group
census['age_group'] = census['age_group'].cat.codes

###############################
