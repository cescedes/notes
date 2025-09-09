##### t-tests in scipy
from scipy.stats import ttest_1samp
import numpy as np

prices = np.genfromtxt("prices.csv")
print(prices)

prices_mean = np.mean(prices)
print("mean of prices: " + str(prices_mean))
#Use ttest_1samp() to run the hypothesis test described above (null: the average price is 1000 Rupees; alternative: the average price is not 1000 Rupees).
# use ttest_1samp to calculate pval
tstat, pval = ttest_1samp(prices, 1000)

# print pval
print(pval)

##############
#some data has been loaded with purchase prices for consecutive days at BuyPie. 
#You can access the first day using daily_prices[0], the second using daily_prices[1], etc.. 
#To practice running a one-sample t-test and inspecting the resulting p-value, try the following:
#1.Calculate and print out a p-value for day 1 where the null hypothesis is that the average purchase price was 1000 Rupees 
#and the alternative hypothesis is that the average purchase price was not 1000 Rupees. Print out the p-value.
#2.Run the same hypothesis tests for days 1-10 (the fastest way to do this is with a for-loop!) and print out the resulting p-values. 
#What’s the smallest p-value you observe for those 10 days?
#3.Try changing the null hypothesis so that the expected population mean that you’re testing against is different from 1000. 
#Try any numbers that you want. How do your p-values change?

from scipy.stats import ttest_1samp
import numpy as np

daily_prices = np.genfromtxt("daily_prices.csv", delimiter=",")

# day 1:
tstat, pval = ttest_1samp(daily_prices[0], 1000)
print("day 1 p-value:")
print(pval)

# 10 days:
for i in range(10):
  tstat, pval = ttest_1samp(daily_prices[i], 1000)
  print("day",i+1, "p-value:")
  print(pval)

# 10 days with a different null hypothesis
print("day 1-10 with a different alternative hypothesis:")
for i in range(10):
  tstat, pval = ttest_1samp(daily_prices[i], 950)
  print("day",i+1, "p-value:")
  print(pval)

