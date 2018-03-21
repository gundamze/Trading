
from pandas import DataFrame, Series
import numpy as np


"""________________________________________________________________________
                           example 1
    1. the parameter summary
    http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot

    2. the matplotlib tutorial
    http://matplotlib.org/users/pyplot_tutorial.html


"""

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('D:/poly/courses/book\python/tutorial/data/spx.csv', index_col=0, parse_dates=True)  # load the data
spx = data['SPX']        # assign the values to another variable, so that keep the original data


# plot one line
fig = plt.figure()                  # open the new plot window
ax = fig.add_subplot(1, 1, 1)       # 1*1 subplot, select the 1st

spx.plot(ax=ax,            # the value to plot on ax
         style='k-',      # k means black, - means solid line, check link 1
         label = 'spx'
        )

# add annotate
crisis_data = [          # a list of tuple
(datetime(2007, 10, 11), 'Peak of bull market'),
(datetime(2008, 3, 12), 'Bear Stearns Fails'),
(datetime(2008, 9, 15), 'Lehman Bankruptcy')
]

for date, label in crisis_data:
    ax.annotate(label,
                xy=(date, spx.asof(date) + 50),         # the arrow location, asof is to return the value at that index
                xytext=(date, spx.asof(date) + 200),    # the text location
                arrowprops=dict(facecolor='black'),     # define the shape of arrow
                horizontalalignment='left',             # the text location
                verticalalignment='top',                # the text location
                )

# add a new line
newline = Series(1200, index = spx.index)
newline.plot(ax = ax,
             style = 'b--',
             label = "new line")

""" you can also add this line to the original data, to form a DataFrame,
    table.plot(style={'column 1 name': 'k-',
                      'column 2 name': 'k--'})
"""

# add legend:
# define the labels of each line, then define the location of legend
ax.legend(loc = 'best')


# Zoom in on 2007-2010
ax.set_xlim(['1/1/2007', '1/1/2011'])
ax.set_ylim([600, 1800])
ax.set_title('Important dates in 2008-2009 financial crisis')
ax.set_xlabel('Date')

# add horizontal line
ax.axhline(y=1400,
           xmin=0.2,                # how far from left edge
           xmax=0.8,                # how far from right edge
           c = 'red',
           linestyle='--',
           linewidth=0.5,zorder=0)

# save plot file
plt.savefig('D:/poly/courses/book\python/tutorial/data/spx.png')



"""________________________________________________________________________
                               bar plot
"""
df = DataFrame(np.random.rand(6, 4),
               index=['one', 'two', 'three', 'four', 'five', 'six'],
               columns = pd.Index(['A', 'B', 'C', 'D'], name='Genus'))


fig, axes = plt.subplots(2, 1)   # 2 rows, 1 column
df.plot(kind='bar',           # vertical bar
        ax=axes[0],           # location
        alpha=0.7)            # opacity, transparent

df.plot(kind='barh', ax=axes[1], alpha=0.7,  # horizontal bar
        stacked = True)

axes[0].set_title('title for plot 1')
axes[1].set_title('title for plot 2')


"""________________________________________________________________________
                               histogram/density
"""

data = pd.read_csv('D:/poly/courses/book\python/tutorial/data/spx.csv', index_col=0, parse_dates=True)  # load the data

data.hist(bins = 50)
import scipy
data.plot(kind='kde')




