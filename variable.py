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

