############################################# data ##########################################

## A. data type
# 1. integer
# 2. float
# 3. string
# 4. range

## B. data structure (structure: the object that contains other objects )
# 1. tuple
# 2. list
# 3. dict (key-value store object)
# 4. set (An unordered collection object for other unique objects, like factor in R)
# 5. matrix (derived from list)

## everything in python is an object, it has method

# check the type(class) of object
x = range(5)
y = list(x)
print(x,
      type(x),      # range is a list
      y,
      type(y)
      )

######################################## 1. integer ############################################
print(1,
      17/3,          # division
      17//3,         # floor, quotient
      17 % 3,        # the remainer of division
      2 ** 7,        # 2 to the power of 7 (2^7)
      round(1.63,1),
      )

x,y = 0,1            # define two var together
print(x,y)

####################################### 2. float ################################################

## every float is store in the form of binary
# e.g. 0.5 is stored in form 1/2 (fraction form, binary form)
x = 0.654               # in the form a/b
print(x,
      x.as_integer_ratio()    # get a and b
      )

## use function in math module
import math
print(math.floor(3.5))

## module decimal could deal with precision of float
import decimal               # import an object decimal, so you could use method of it
from decimal import Decimal  # import an object Decimal

print(decimal.getcontext(),  # check the current precision and other options,
      Decimal(1),
      Decimal(11),
      Decimal(1)/Decimal(11),
      1/11,
     )

decimal.getcontext().prec = 4         # lower precision than default, prec default is 28

print(decimal.getcontext(),           # check the current precision and other options,
      Decimal(1),
      Decimal(11),
      Decimal(1)/Decimal(11),
      1/11,
     )

##################### 3. string (character) ###############

print( "this is string. \"quote\" ",                           # \ is to cite the sign " or '

       "go to new line \n this should be second line",         # \n is translated to new line

       "c:\name",            # \n is new line

       r"c:\name",           # put r in ahead

      """
      first
      second
      third\
      """,         # quote multiple lines, the \ is to prevent from creating new line

      3 * "ryan " + 3 * "yu ",

      "ryan" " yu",      # the same to + operator, concantenate, u'd better to use +
)


x = "123456"
print(x,
      x[0],          # index/position is 0, should be the first letter
      x[-1],         # the last letter
      x[2:5],        # index 2 is included, 5 is excluded
      x[2:],         # from index 2 to the last one
      len(x),
      )

# note: u can not assign a value to the index one

### method of string

x = "this, is string"
x1 = x.capitalize()     # make the first letter in big-case
x2 = x.split()          # split it to a list of words
x.split('s',1)          # split only 1 time by s
x21 = ' '.join(x2)      # combine a list of string to one string, like multiple + operation
x3 = x.find('string')   # return the index of letter "s" in the string
x4 = x.find('Python')   # not in the string, return -1
x5 = x.replace(' ', '|')

x6 = 'http://www.python.org'.strip('htp:/')    # only left www.python.org, just write head and tail letters of a string
[a.strip() for a in x.split(',')]    # a.strip to remove the blank
x.lower()
x.upper()
x.index(',')

print(x,x1,x2,x3,x4,x5,x6)

# convert a character to ASCII value
ord("a")



""" ### module re to deal with string ###
"""
#################### example 1
series = """
'01/18/2014 13:00:00', 100, '1st';
'01/18/2014 13:30:00', 110, '2nd';
'01/18/2014 14:00:00', 120, '3rd'
"""   # series is a string in multiple lines

import re
dt = re.compile("'[0-9/:\s]+'")
type(dt)     # dt is the pattern in which you deal with string
result = dt.findall(series)       # result is the list of date

################## example 2

text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex = re.compile(pattern, flags=re.IGNORECASE)     # re.IGNORECASE makes the regex case-insensitive
regex.findall(text)


### replace or insert a string

"Hello %s, my name is %s" % ('john', 'mike')      # Hello john, my name is mike".

"My name is %s and i'm %d" % ('john', 12)         # My name is john and i'm 12
#### note: it is much better than to use the operator +, because it is easy to read and more efficient



################## unicode string ####################

x = u'DE0007600801\u200b'
type(x)

str(x)

isinstance(x, unicode)

from django.utils.encoding import smart_str
y = smart_str(x)
type(y)

y.strip('\xe2\x80\x8b')


z = 0.123
z.is_float

######################## B. data structure #################


# range is a special list, three parameters, start, stop, step,

# range can not contain float, but u can write a float frange funcion
def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

for i in frange(0.5,1.01,0.1):
    print(i)


######################## B. data structure #################
# create these variables

xlist= [1,2,3,4,5,6]                          # list
xtuple= (1,"apple")                           # tuple
xdic={'a':2, 'b':3}                           # dict
xset = {2,3,3,3,3,6}                          # set

### difference between list and tuple ###

# tuple: If you went for a walk, you could note your coordinates at any instant in an (x,y) tuple.
# list: If you wanted to record your journey, you could append your location every few seconds to a list.

# tuple: have the structure
# list: have the order

# tuple: immutable, xtuple[1] = "tomato" is error
# list: mutable

# tuple: store for heterogeneous
# list: store for homogeneous (usually)


######################## 1. tuple ####################

# nested
x1=[xtuple, (2,"orange"), (3,"banana")]
x2 = ( (xtuple, (2, "orange")), (3, "banana") )
x22 = xtuple, (2,"orange"), (3, "banana")
x3 = ( [1,2,3], [4,5,6] )

x = (2008, 11, 12)
x += (1,2,3)

print(x1,
      type(x1),
      x1[0],
      x1[0][1],
      type(x1[0]),
      x2,
      x2[0],
      x22,
      x3,
     )

### tuple method
print(xtuple.count('apple'),    # the number of occurrences
      xtuple.index(1),          # return index
      list(xtuple),              # convert tuple to list
    )


######################### 2. list ##############################
# list is the most powerful data type in python
# a vector is a list
x = [1,4,9,16,25]

# range, a sequence of number is list
type(range(9))

print(x,
      type(x),
      x[0],            # list is kind of index-value pair object
      x[-1],
      x[:-2],          # -2 index is 16, but not include
      x + [36,49],     # add in the end of list
      len(x),
      x[::2],          # return the all by the step 2
      )

### assign the value
x[0] = 1             # u can assign a value to index one
x[1]=[]              # remove the second element
x[:]=[]              # cite all the items in list, and clear the list

1 in shoplist       # check whether 1 is in the list
23 not in shoplist

### method for list

x.append([4,5])    # append a list at the end [1,2,3,[4,5]]
x.extend([6,7])    # extend elements [1,2,3,6,7]
x.insert(0,-1)     # add -1 in the ahead of 0 index(first element)
x.remove(-1)       # remove value -1
y = x.pop(3)       # for x , remove the index 3
                   # for y, the value of index 3
                   # remove not return the "deleted" value for y
x.pop()            # pop the last element
x.pop(len(x)-1)    # same to above

x.index(3)         # return the index of value 3 in the first time
x.count(3)         # count the number of times value 3 appears
x.reverse()
x.sort()
x.clear()

del x[1:2]         # delete the value at index 1 to 2, it not to return a value compared with pop method
del x[:]           # delete the items in list x, but x exist
del x              # delete the var x, x not exist


### create a list

from random import randint

print([['a','b','c'],[1,2]])                              # list could store diff type and length of data
print([x**2 for x in range(0,10,2)])                      # range(start,end+1, step)
print([(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y])
print([randint(0, 10) for i in range(100)])               # 100 random integers between 0 and 10




# matrix is a list
xmatrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    ]
# transpose of matrix
print([[row[i] for row in xmatrix]for i in range(4)])  # i = 1, then [row[1] for row in matrix],  this is to transpose the matrix

print(list(zip(*xmatrix)))        # zip is to transpose the xmatrix

for i, v in enumerate(xmatrix):   # enumerate is to return index as i, value in list as v
    print(i,v)


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):                      # zip could regard entries as pairs
    print("what is your {0}? It is {1}."  .format(q,a))   # {0} refer q, {1} refer a when you set format


### computation

print([x**2 for x in range(10)])         # compute for each element in a list
print(map(lambda x: x**2, range(10)))    # apply a function to each element, first input of map is the function,

def even(x):             # define a function which returns boolean
    return x % 2 == 0
map(even, range(10))     # apply function even to each element , like apply() in R
filter(even, range(10))  # return the value when boolean is true, like which() in R

from functools import reduce
reduce(lambda x,y: x+y, range(10))
# 1: x=1,y=2, newlist = [3,3,4,5,6...]
# 2: x=3,y=3, newlist = [6,4,5,6,...]
# 3: x=6,y=4, newlist = [10,5,6,...]
# to get the sum of 1 to 10


### missing value
x = [1,3,'','abc']
x[1:3] == ''
y = pd.Series(x)
y == ''
np.all(y != '')

######################## 3. dict (key-value) ########################

xdic= {"name":"ryan", "id":123456}     # dictionary, unordered and unsortable
xdic["status"] = "student"
# create a empty dictionary, use initial value
x = {}
type(x)


print(xdic)
print(type(xdic))
print(xdic["name"])

xdic.get("name",1) # if key: name is not available, then return 1
xdic.get("abc",1) # if key: name is not available, then return 1




### method
print(
    xdic.keys(),    # check the keys
    xdic.values(),
    xdic.items(),   # return key-value pair, in python 2 it is .iteritems()

)


for i in xdic:
    print(i)        # address is a dictionary, it returns the keys

for i in xdic:
    print(xdic[i])     # returns the values in dictionary

for k,v in xdic.items():
    print(k,v)  # return the real value


"status" not in xdic

x = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])   # convert list to dict
{x: x**2 for x in (2, 4, 6)}      # create a key-value pairs


######################## 4. set ########################

# no oder
# no duplicate value, unique value
x = {'apple', 'apple','banana'}
x
type(x)
'apple' in x
'orange' in x

### compuation
x = set(['u', 'd', 'ud', 'du', 'd', 'du'])   # convert list to set
a = set('abracadabra')    # convert string to set
b = set('alacazam')
print(a ,
      b ,
      a-b ,      # letters in a but not b
      a | b ,    # in a or b
      a & b ,    # in a and b
      a ^ b ,    # in a or b but not both
      )

### method
s = set(['u', 'd', 'ud', 'du', 'd', 'du'])
t = set(['d', 'dd', 'uu', 'u'])
s.union(t)        # all of s and t
s.intersection(t) # both in s and t
s.difference(t)   # in s but not t
t.difference(s)   # in t but not s
s.symmetric_difference(t) # in either one but not both

from random import randint
l = [randint(0, 10) for i in range(1000)]   # 1,000 random integers between 0 and 10






###########  format ################
print('the {} who say {}'.format('Tom','hi',100))
print('the {0} who say {0}'.format('Tom','hi',100))
print('the {1} who say {1}'.format('Tom','hi',100))
print('the {0:5} who say {2:5}'.format('Tom','hi',100))           # give 5 space behind a str, and 5 space ahead of integer
print('the {0} who say {2:5.3f}'.format('Tom','hi',192.45678))    # give 5 space of the integer at least, just remain 3 digit decimals

for i in range(1,11):
    print('{:2d}{:3d}{:4d}'.format(i,i*i,i**3))      # d means intger, 4d means 4 digit integer

# it is much better than the following table
for i in range(1,11):
    print(i,i*i, i**3)


