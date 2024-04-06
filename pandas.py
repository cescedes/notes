import pandas as pd

#create a dataframe
df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name':['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
})

#create a dataframe w/ keyword columns
df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
],
  columns=[
    'Store ID', 'Location', 'Number of Employees'
  ])

#read csv
df = pd.read_csv('sample.csv')

#load the CSV:
df = pd.read_csv('imdb.csv')
print(df.head())
print(df.info())

########
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north = df['clinic_north']
print(type(clinic_north)) #<class 'pandas.core.series.Series'>
print(type(df)) #<class 'pandas.core.frame.DataFrame'>

#select multiple columns
clinic_north_south = df[['clinic_north', 'clinic_south']]
print(type(clinic_north_south)) #<class 'pandas.core.frame.DataFrame'>

#select row
march = df.iloc[2]
#When we select a single row, the result is a Series (just like when we select a single column).
#select multiple rows
april_may_june = df.iloc[3:6]

#select rows with logic
january = df[df.month == 'January']
march_april = df[(df.month == 'March') | (df.month == 'April')]
# select rows with logic, the isin command to check that df.month is one of a list of values:
january_february_march = df[df.month.isin(['January', 'February', 'March'])]

#When we select a subset of a DataFrame using logic, we end up with non-consecutive indices. 
#This is inelegant and makes it hard to use .iloc().
#We can fix this using the method .reset_index().
df2 = df.loc[[1, 3, 5]]  #the subset with indexes 1,3,5
df3 = df2.reset_index()
#the old indices have been moved into a new column called 'index'. 
# Unless you need those values for something special, 
#it’s probably better to use the keyword drop=True so that you don’t end up with that extra column. 
#If we run the command df.reset_index(drop=True), we get a new DataFrame
#If we use the keyword inplace=True we can just modify our existing DataFrame.
df2.reset_index(inplace = True, drop = True)

##################

#Load the data from shoefly.csv into the variable orders.
orders = pd.read_csv('shoefly.csv')
#Inspect the first 5 lines of the data.
print(orders.head())
#Select all of the email addresses from the column email and save them to a variable called emails.
emails = orders['email']
#Frances Palmer claims that her order was wrong. What did Frances Palmer order?
#Use logic to select that row of orders and save it to the variable frances_palmer.
frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]
#Select all orders for shoe_type: clogs, boots, and ballet flats and save them to the variable comfy_shoes.
comfy_shoes = orders[(orders.shoe_type == 'clogs') | (orders.shoe_type == 'boots') | (orders.shoe_type == 'ballet flats')]
