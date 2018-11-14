# 
# Phil Tenteromano
# 11-5-2018
#
# Plotting NYC temperature data using 
# numpy, pandas, matplotlib, and a csv dataset

import pandas as pd
import matplotlib.pyplot as plt

# 21264 rows x 12 columns
data = pd.read_csv("./data/NYC_temps.csv")

# convert time data into datetime object
data['DATE'] = pd.to_datetime(data['DATE'])

# Central park only data - 10632 rows × 12 columns
central_park = data.loc[data['STATION'] == 'USW00094728']

# get 2017 data, then group into months
twenty17 = central_park[ central_park.DATE.dt.year == 2017 ]
twenty17monthly = twenty17.groupby(twenty17.DATE.dt.month)

# get the high for each month
high2017 = twenty17monthly.TMAX.max()

# get the low for each month
low2017 = twenty17monthly.TMIN.min()

# 2017 high and low for all 12 months
# plot both onto one plot
plt.ylabel('Temperature')
plt.title('2017 Temperature High/Low')
plt.xlabel('Months')
plt.grid(True)
plt.plot(high2017, 'r')
plt.plot(low2017, 'b')
plt.show()

# all data from 1990 - 2016
# bitwise, using a boolean Mask then get the range
boolMask = (central_park.DATE.dt.year >= 1990) & (central_park.DATE.dt.year <= 2016)
ninetyTo2016 = central_park.loc[boolMask]

# get the monthly data from 1990 - 2016
monthly = ninetyTo2016.groupby(ninetyTo2016.DATE.dt.month)

highs1990_2016 = monthly.TMAX.max()
lows1990_2016 = monthly.TMIN.min()

# plot the data onto the same plot
plt.ylabel('Temperature')
plt.title('1990-2016 Monthly Average High/Low')
plt.xlabel('Months')
plt.grid(True)
plt.plot(highs1990_2016, 'r')
plt.plot(lows1990_2016, 'b')
plt.show()
