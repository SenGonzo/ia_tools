%matplotlib notebook
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import *
import matplotlib as mpl

# Get Data
url = 'https://raw.githubusercontent.com/SenGonzo/IA-Py/master/926823.csv'
df = pd.read_csv(url,header=0)

# Clean it a bit
df = df[(df['AWND'] != -9999.0)]

# Year of interest
df_2016 = df[(df['DATE'] >= 20160101)]


# Rotate to North = 90 instead of 0, create Season
for index, row in df.iterrows():
    if row['WDF2'] >= 270:
        row['WDF2'] -= 270
    else:
        row['WDF2'] += 90


r = df_2016['AWND']
theta = df_2016['WSF2']
colors = df_2016['DATE']
cmap = plt.cm.get_cmap('viridis')

fig, ax = plt.subplots()
ax = subplot(111, polar=True)
c = scatter(theta, r, c=colors, cmap=cmap)
c.set_alpha(0.75)
ax.set_xticklabels(['East', '', 'North', '', 'West', '', 'South'])
ax.set_yticklabels(['5 MPH', ' 10 MPH', '15 MPH', '20 MPH', '25 MPH'])
ax.set_title('2016 Wind Speed and Direction in Ann Arbor Michigan')
# plt.colorbar(c)

cbar = fig.colorbar(c, ticks=[20160115, 20160215, 20160315, 20160415, 20160515, 20160615, 20160715, 20160815,
                             20160915, 20161015, 20161115, 20161215,], orientation='horizontal')
cbar.ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apl', 'May', 'June', 'July',
                         'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])

show()