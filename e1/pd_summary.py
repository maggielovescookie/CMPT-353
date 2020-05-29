#Qianhui Xu - CMPT353 2020 Summer

import pandas as pd 

totals = pd.read_csv('totals.csv').set_index(keys=['name'])
counts = pd.read_csv('counts.csv').set_index(keys=['name'])

# Which city had the lowest total precipitation over the year? 
# Hints: sum across the rows (axis 1); use argmin to determine which row has the lowest value. 
# Print the row number.

#Reference: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.min.html
sumPerCity = totals.sum(axis=1)
lowestPrecip = pd.Series.idxmin(sumPerCity)
print('City with lowest total precipitation: \n' + str(lowestPrecip))



# Determine the average precipitation in these locations for each month. That will be the total precipitation for each month (axis 0), divided by the total observations for that months. 
# Print the resulting array.

sumPerMonth = totals.sum(axis=0)
obsPerMonth = counts.sum(axis=0)
avgPrecipPerMonth = sumPerMonth/obsPerMonth

print('Average precipitation in each month: \n' + str(avgPrecipPerMonth))


# Do the same for the cities: give the average precipitation (daily precipitation averaged over the month) for each city by printing the array.

obsPerCity = counts.sum(axis=1)
avgPrecipPerCity = sumPerCity / obsPerCity
print('Average precipitation in each city: \n' + str(avgPrecipPerCity))
