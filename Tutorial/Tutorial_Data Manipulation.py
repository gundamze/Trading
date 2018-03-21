
""" __________________________________________________________
                 discretization and binning
                put continuous data into bins
    ___________________________________________________________
"""
import pandas as pd
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']

cats = pd.cut(ages, bins, right = False, labels = group_names)
cats

cats.labels          # like index of range
cats.levels          # the bin range, [18:25), or the labels name, 'Youth',

pd.value_counts(cats)    # count in each bin

### second example
import numpy as np
data = np.random.rand(20)
cats = pd.cut(data, 4, precision=2)    # put them into quartile
pd.value_counts(cats)

cats1 = pd.qcut(data, 4, precision=2)  # qcut could keep the same number in each bin
pd.value_counts(cats1)

cats2 = pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.],precision=2)   # set your own quantile
pd.value_counts(cats2)

"""______________________________________________________________
                       Outliers
   _____________________________________________________________
"""
np.random.seed(12345)
data = DataFrame(np.random.randn(1000, 4))    # 1000 rows, 4 column. 4 line of 1000 pints
data.describe()

data.head()

col = data[3]    # pick out the last column

col[np.abs(col) > 3]    # pick out the outliers when it exceed 3 or -3

data[(np.abs(data) > 3).any(1)]    # 1 means check the rows, any True returns True, pick out the outliers in any column

data[np.abs(data) > 3] = np.sign(data) * 3    # set the outliers value to 3 or -3
data.describe()


"""_______________________________________________________________________
                       dummy
   _______________________________________________________________________
"""

df = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                'data1': range(6)})
pd.get_dummies(df['key'],    # key has 3 distinct value, want to get a matrix with 3 column with 1 or 0 values
               prefix='key') # prefix is to change the column name

"""_______________________________________________________

"""

"""######### check #########"""
######### for a list/str ########
a = []
type(a)
not a
len(a) != 0

############## for a object/series #########
a.empty         # return True or Flase
not a.empty






