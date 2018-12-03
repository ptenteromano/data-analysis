# 
# Phil Tenteromano
#
# 11-5-2018
#
# Comparing baby names from 2000 to 2016
#

import pandas as pd
import matplotlib.pyplot as plt

babies00_raw = pd.read_csv('./data/babyNames2000.txt', names=['name', 'sex', 'births'])
babies16_raw = pd.read_csv('./data/babyNames2016.txt', names=['name', 'sex', 'births'])

babies00 = babies00_raw.sort_values('births', ascending=False)
babies16 = babies16_raw.sort_values('births', ascending=False)

a = babies00.head(20)
b = babies16.head(20)
c = pd.merge(a, b, on='name', how='outer', suffixes=('2000', '2016'))

# plot from the pandas object
c.plot(x='name', kind='bar')
# this is necessary to show the plots (but may not be in jupyter notebook)
plt.show() 

# graph on last letter
# add last letter
babies16_raw['lastletter'] = babies16_raw['name'].str[-1:]
last_letter = babies16_raw.groupby(babies16_raw['lastletter'])
# plot data
last_letter.max().plot(kind='bar')
plt.show()
