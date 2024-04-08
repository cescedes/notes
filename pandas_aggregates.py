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

###################

#A/B Testing for ShoeFly.com
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
#Examine the first few rows of ad_clicks.
print(ad_clicks.head())

#How many views (i.e., rows of the table) came from each utm_source?
print(ad_clicks.groupby('utm_source').user_id.count().reset_index())

#If the column ad_click_timestamp is not null, then someone actually clicked on the ad that was displayed.
#Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise.
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

#We want to know the percent of people who clicked on ads from each utm_source.
#Start by grouping by utm_source and is_click and counting the number of user_id‘s in each of those groups. 
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)

#pivot the data so that the columns are is_click (either True or False), the index is utm_source, and the values are user_id.
clicks_pivot = clicks_by_source.pivot(columns = 'is_click', index = 'utm_source', values = 'user_id').reset_index()
print(clicks_pivot)

#Create a new column in clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source.
clicks_pivot['percent_clicked'] =  clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot)

#The column experimental_group tells us whether the user was shown Ad A or Ad B. Were approximately the same number of people shown both ads?
print(ad_clicks.groupby('experimental_group').user_id.count().reset_index())

#Using the column is_click that we defined earlier, check to see if a greater percentage of users clicked on Ad A or Ad B.
print(ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index().pivot(columns = 'is_click', index = 'experimental_group', values = 'user_id').reset_index())

#The Product Manager for the A/B test thinks that the clicks might have changed by day of the week.
#Start by creating two DataFrames: a_clicks and b_clicks, which contain only the results for A group and B group, respectively.
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

#For each group (a_clicks and b_clicks), calculate the percent of users who clicked on the ad by day.
a_clicks_pivot = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(columns = 'is_click', index = 'day', values = 'user_id').reset_index()

a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True] / a_clicks_pivot[True] + a_clicks_pivot[False]
print(a_clicks_pivot)

b_clicks_pivot = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(columns = 'is_click', index = 'day', values = 'user_id').reset_index()

b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True] / b_clicks_pivot[True] + b_clicks_pivot[False]
print(b_clicks_pivot)

####################


