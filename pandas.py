import pandas as pd

#create a dataframe
df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name':['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
})
#the lists should have equal number of elements

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

#####################

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

#adding a column
df['Quantity'] = [100, 150, 50, 35]
df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']
df['Is taxed?'] = 'Yes' #apply to all rows
#Add a column to df called 'Margin', which is equal to the difference between the Price and the Cost to Manufacture.
df['Margin'] = df.Price - df['Cost to Manufacture']

#the apply function to apply a function to every value in a particular column.
#this code overwrites the existing 'Name' columns by applying the function upper to every row in 'Name'.
df['Name'] = df.Name.apply(str.upper)
#Apply the function lower to all names in column 'Name' in df. Assign these new names to a new column of df called 'Lowercase Name'. 
df['Lowercase Name'] = df.Name.apply(str.lower)

#a lambda function get_last_name which takes a string with someone’s first and last name (i.e., John Smith), and returns just the last name (i.e., Smith).
get_last_name = lambda name: name.split(' ')[-1]
#Use the lambda function get_last_name to create a new column last_name with only the employees’ last name.
df['last_name'] = df.name.apply(get_last_name)

#We can also operate on multiple columns at once. 
#If we use apply without specifying a single column and add the argument axis=1,
#the input to our lambda function will be an entire row, not a column.
#If an employee worked for more than 40 hours, she needs to be paid overtime (1.5 times the normal hourly wage).
#Create a lambda function total_earned that accepts an input row with keys hours_worked and hourly_wage and uses an if statement to calculate the total wages earned.
total_earned = lambda row: row['hourly_wage'] * row['hours_worked'] if row['hours_worked'] <= 40 else row['hourly_wage'] * 40 + row['hourly_wage'] * 1.5 * (row['hours_worked'] - 40)
#Use the lambda function total_earned and apply to add a column total_earned to df with the total amount earned by each employee.
df['total_earned'] = df.apply(total_earned, axis = 1)

#renaming columns
df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18]
})
df.columns = ['First Name', 'Age']

#renaming columns. with rename method we can just change a single column name. it creates a new dataframe so we use inplace=True to overwrite.
df.rename(columns={'name': 'movie_title'}, inplace=True)

#######################

#Add a new column called shoe_source, which is vegan if the materials is not leather and animal otherwise.
orders['shoe_source'] = orders.shoe_material.apply(lambda x: 'vegan' if x != 'leather' else 'animal')
#Using the columns last_name and gender create a column called salutation which contains Dear Mr. <last_name> for men and Dear Ms. <last_name> for women.
orders['salutation'] = orders.apply(lambda row: 'Dear Mr. ' + row['last_name'] if row['gender'] == 'male' else 'Dear Ms. ' + row['last_name'], axis=1)

###################

import pandas as pd
#Data for all of the locations of Petal Power is in the file inventory.csv. Load the data into a DataFrame called inventory.
inventory = pd.read_csv('inventory.csv')
#Inspect the first 10 rows of inventory.
print(inventory.head(10))
#The first 10 rows represent data from your Staten Island location. Select these rows and save them to staten_island.
staten_island = inventory.iloc[:10]
#A customer just emailed you asking what products are sold at your Staten Island location. 
#Select the column product_description from staten_island and save it to the variable product_request.
product_request = staten_island['product_description']
#Another customer emails to ask what types of seeds are sold at the Brooklyn location.
#Select all rows where location is equal to Brooklyn and product_type is equal to seeds and save them to the variable seed_request.
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
#Add a column to inventory called in_stock which is True if quantity is greater than 0 and False if quantity equals 0.
inventory['in_stock'] = inventory.apply(lambda row: True if row.quantity > 0 else False, axis=1)
#Create a column called total_value that is equal to price multiplied by quantity.
inventory['total_value'] = inventory['price'] * inventory['quantity']
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
#Using combine_lambda, create a new column in inventory called full_description that has the complete description of each product.
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
