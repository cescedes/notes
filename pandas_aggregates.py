# mean	Average of all values in column
# std	Standard deviation
# median	Median
# max	Maximum value in column
# min	Minimum value in column
# count	Number of values in column
# nunique	Number of unique values in column
# unique	List of unique values in column
#syntax: df.column_name.command()

#the price of the most expensive pair of shoes purchased.
most_expensive = orders.price.max()

#how many different colors of shoes
num_colors = orders.shoe_color.nunique()

#the most expensive shoe for each shoe_type using groupby()
pricey_shoes = orders.groupby('shoe_type').price.max()  #the object type is series
pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()  #the object type is dataframe

#the 25th percentile for shoe price for each shoe_color to help Marketing decide if we have enough cheap shoes on sale.
cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()

#Create a DataFrame with the total number of shoes of each shoe_type/shoe_color combination purchased. Save it to the variable shoe_counts.
shoe_counts = orders.groupby(['shoe_type','shoe_color']).id.count().reset_index()
#Reorganizing the table - pivot table
#to compare purchases of different shoe colors of the same shoe type by creating a pivot table.
shoe_counts_pivot = shoe_counts.pivot(columns = 'shoe_color', index = 'shoe_type', values = 'id').reset_index()

###################

#The column utm_source contains information about how users got to ShoeFly’s homepage.
#Use a groupby statement to calculate how many visits came from each of the different sources. 
click_source = user_visits.groupby('utm_source').id.count().reset_index()
#Use groupby to calculate the number of visits to our site from each utm_source for each month. 
click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()
#Use pivot to create a pivot table where the rows are utm_source and the columns are month.
click_source_by_month_pivot = click_source_by_month.pivot(columns = 'month', index = 'utm_source', values = 'id').reset_index()



