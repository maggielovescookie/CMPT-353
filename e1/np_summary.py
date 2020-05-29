#Qianhui Xu - CMPT353 2020 Summer

import numpy as np
data = np.load('monthdata.npz')
totals = data['totals']
counts = data['counts']

# Which city had the lowest total precipitation over the year? 
# Hints: sum across the rows (axis 1); use argmin to determine which row has the lowest value.
# Print the row number.

sumPerCity = totals.sum(axis=1)
lowestPrecip = np.argmin(sumPerCity)
print('Row with lowest total precipitation: \n' + str(lowestPrecip))


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


# Calculate the total precipitation for each quarter in each city (i.e. the totals for each station across three-month groups). You can assume the number of columns will be divisible by 3. 
# Hint: use the reshape function to reshape to a 4n by 3 array, sum, and reshape back to n by 4.

reshapedT = totals.reshape(-1 , 3)
quaterPrecip = reshapedT.sum(axis=1).reshape(-1,4)

print('Quarterly precipitation totals: \n ')
print(str(quaterPrecip))
