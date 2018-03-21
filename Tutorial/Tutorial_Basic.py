######## python tutorial basic ##############

######## how to make comment ###########
# single line comment 
"""
 multiple   line
"""

"""
################################# several ways to run python ######################################

1. "Python (command line)" open a "python.exe" file -> console (like cmd)

2. "IDLE (Python GUI)" - (Integrated DeveLopment Environment)
 2.1. shell window -> console
 2.2. editor window -> script

4. ipython notebook (interactive computational environment)

shift + right click "script" > open command window here > ipython notebook > ... 

pro: could run code line by line, do not compile the file at first

the location of the notebook is in the folder:
    D:\tool\Canopy\User\Scripts
    D:\tool\python directory\Scripts\mynotebook
    first is python 2.7, second is python 3.4, we use the second because we could create a notebook folder

the file type is .ipynb
the python code file do not store the data

5. IDE
 5.1. IDLE: right click .py file -> edit with IDLE -> go to 2.2.
 5.2. Canopy
    pro: do not install the packages one by one
 5.3. Pycharm -> favorite
 5.4. Pythonwin


"""

"""
######################## install modules #############################
    
## install modules (first way)
# cmd in the path d/too/python directory/scripts
# then type: pip install numpy
## error: unable to find vcvarsall.bat
# use the second way

## update
# cmd in the path d/tool/path/directory
# then type: pip install --update numpy

## check the list of modules
# cmd path:  d/tool/pathon directory
# then type: help('modules')

## installation (second way) ###################### the successful way ####################
# link: http://www.lfd.uci.edu/~gohlke/pythonlibs/
# search your module, 32 bit, python 3.4, wheel file, and download it in the "scripts" file folder
# cmd path: d/tool/pathon module/Scripts
# type: pip install "module name.whl"


"""
"""
######################## run selection part in Pycharm #############################
alt + shift + E

"""
# check your current working dictionary  

import os          # import the module(library), os
print(os.getcwd()) # tell you where is your script


### check python version 

import sys
print (sys.version)

### check all variables 
x = 1
print(dir()) # list the variable names



######################## function #########################

# define a function x+y and y has default value 3, define z with global value 3
''' you dont need to declare the variables in python '''
def func2(x,y=3):   # must have ":"
    global z        # declare the global name
    z = 3
    g = input("enter name here: ")
    print('welcome' + g)
    type(g)
    return x+y      # must return a value

    
# note: x and y are the local variables, when u use that function u can call the local value


########################## statement #########################

### 1. if ###

x = int(input("\nplease enter an integer "))
if x<0:
    print("this is negative")
elif x==0:
    print("this is zero")
else:
    print("this is positive")


### 2. for ###

words = ["cat", "window", "defenestrate"]
for w in words:
    print(w, len(w))


for i in range(5):       # from 0 to 4
    print(i)

for i in range(2,10,2):  # from 2 to 9 step of 2
    print(i)


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)


### 3. while ###

x = int(input('enter a number less than 5'))
while x < 5:
    x += 1
    print(x)
    

# to break in the while statement
x = float(input('enter a number less than 20'))
while True:
    x+=1
    print(x)
    if x == 20:
        break


########################### modules ############################


# import the modules (like packages/library in R) 
import math
math.sqrt(16)
# u have to cite the module name
from math import sqrt
sqrt(16)

# u don't have to cite the module name, but it is not recommended
myfloor = math.floor
myfloor(4.4)

# check all the function in module math
help(math)

# to stop the program in command line (DOC)
input()

# convert input type, str, into integer
x = int(input('age: '))
print(x+2)



