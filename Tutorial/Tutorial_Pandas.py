################### data structure ######################
dir()

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from numpy import nan as NA

"""
1. series (one-dimensional array like)
2. data frame
3. index
"""
"""________________________________________________________________
                        Series
"""

obj = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

obj
obj.values
obj.index

obj[[2,1]]        # sequence index
obj[['a','c']]    # defined index
obj[obj > 0]

# from dictionary
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
type(sdata)
type(sdata['Ohio'])              # this is scalar value

obj3 = Series(sdata)             # convert dictionary to series, key is index, value is value
type(obj3)
obj3.name = 'population',        # change the name for value, like column name
obj3.index.name = 'state',       # change the name for index, like row name

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)       # return the partial series based on index, totally matched with index



""" #################### operation ######################### """
obj4 + obj3     # add the values based on index

"""________________________________________________________________
                        DataFrame
"""

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
type(data)                      # this is dict
type(data['state'])            # this is list, not a single scalar value

frame = DataFrame(data,
                  columns=['year', 'state', 'pop', 'debt'],           # re-order and add new column
                  index=['one', 'two', 'three', 'four', 'five'])      # define index)

frame
frame.values                # output by each index
frame.index                # index is immutable, can not be modified
frame.columns              # return column names

frame['state']             # return a column
frame.state                # the same to above

frame.ix['three',['year','state','pop']]     # return a row and columns
frame.ix[['three','four'],[0,3,2]]           # based on column sequence


########## change the value based on index
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame['debt'] = val        # assign the value to a column of frame based on index

######### add a new column
frame['eastern'] = frame.state == 'Ohio'     # add a Series
frame

######## drop
frame.drop('five', axis = 0)        # drop a row, return the data frame, 0 means drop the row, but it not change frame itself
frame.drop('debt', axis = 1)        # drop a column

del frame['eastern']                # forever, do not return




