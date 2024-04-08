import pandas as pd

sales = pd.read_csv('sales.csv')
targets = pd.read_csv('targets.csv')

#merge dataframes with pd.merge
sales_vs_targets = pd.merge(sales, targets)
#Select the rows from sales_vs_targets where revenue is greater than target. 
crushing_it = sales_vs_targets[sales_vs_targets['revenue'] > sales_vs_targets['target']]

sales = pd.read_csv('sales.csv')
targets = pd.read_csv('targets.csv')
men_women = pd.read_csv('men_women_sales.csv')
#merge all three dataframes with merge() method
all_data = sales.merge(targets).merge(men_women)
#Select the rows of all_data where: revenue is greater than target AND women is greater than men
results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]

#merge on specific columns, use .rename() to merge two DataFrames whose columns don’t match.
orders_products = pd.merge(orders, products.rename(columns={'id': 'product_id'}))

#the keywords left_on and right_on to specify which columns we want to perform the merge on.
#Merge orders and products using left_on and right_on. Use the suffixes _orders and _products. 
orders_products = pd.merge(orders, products, left_on = 'product_id', right_on = 'id', suffixes = ['_orders', '_products'])

#mismatched merges / when there's a mismatched value we lose the unmatched rows.
#we could use an Outer Join. 
#An Outer Join would include all rows from both tables, even if they don’t match. 
#Any missing values are filled in with None or nan (which stands for “Not a Number”).
store_a_b_outer = pd.merge(store_a, store_b, how='outer')

#A Left Merge includes all rows from the first (left) table, but only rows from the second (right) table that match the first table.
store_a_b_left = pd.merge(store_a, store_b, how='left')  #The items with null in store_b_inventory are carried by Store A, but not Store B.
store_b_a_left = pd.merge(store_b, store_a, how='left')  #the items with null are not carried by Store A, but are carried by Store B
#right merge opposite

#reconstruct a single DataFrame from multiple smaller DataFrames, we can use the method pd.concat([df1, df2, df3, ...]).
#This method only works if all of the columns are the same in all of the DataFrames.
menu = pd.concat([bakery, ice_cream])



