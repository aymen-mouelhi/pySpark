# Basic Tutorials for python

s = "test function of tab completion"

# type s.<TAB> to see the suggestions
len(s.split(' '))
# Show your experiments working on a string.
# Try splitting a string into its constituent words, and count the number of words.

# Indentation in Python

language = "Python"
if language == "Python":
    x = 10
    x += 10
    y = 5 # all statements in the same block must have the same indentation
    y = (
        x + y
    ) # statements can be on multiple lines, using ( )
    print (x
           + y)

    # statements can also be split on multiple lines by using \ at the END of each line
    x = y \
        + y

    # do some other stuffs
elif language == "Java":
    # another block
    pass
else:
    # another block
    pass


# Ternary conditional operator
x = 10
# a very natural way
y = 5 if x > 10 else 15
print(y)

# another way
y = x > 10 and 5 or 15
print(y)

# Loops
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Python has no built-in array data structure
# instead, it uses "list" which is much more general
# and can be used as a multidimensional array quite easily.
for element in array:
    print(element)

# Get Index
for (index, element) in enumerate(array):
    print(index, element)



# 2-dimentions array with 4 rows, 3 columns
twod_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
for index, row in enumerate(twod_array):
    print("row ", index, ":", row)

# print row 1 until row 3
print("row 1 until row 3: ", twod_array[1:3])

# all rows from row 2
print("all rows from row 2: ", twod_array[2:])

# all rows until row 2
print("all rows until row 2:", twod_array[:2])

# all rows from the beginning with step of 2.
print("all rows from the beginning with step of 2:", twod_array[::2])


# Dictionaries
d = {'key1': 'value1', 'key2': 'value2'}  # Create a new dictionary with some data
print(d['key1'])       # Get an entry from a dictionary; prints "value1"
print('key1' in d)     # Check if a dictionary has a given key; prints "True"
d['key3'] = 'value3'    # Set an entry in a dictionary
print(d['key3'])      # Prints "value3"
# print(d['key9'])  # KeyError: 'key9' not a key of d
print(d.get('key9', 'custom_default_value'))  # Get an element with a default; prints "custom_default_value"
print(d.get('key3', 'custom_default_value'))    # Get an element with a default; prints "value3"
del d['key3']        # Remove an element from a dictionary
print(d.get('key3', 'custom_default_value')) # "fish" is no longer a key; prints "custom_default_value"

# Funcitons
def square(x):
    return x*x

print(square(5))

# Lambda functions
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# apply function "square" on each element of "array"
print(list(map(lambda x: square(x), array)))

# or using a for loop, and a list comprehension
print([square(x) for x in array])

print("orignal array:", array)

# Closures ?
# select only the prime number in array
# and square them
def filterAndSquarePrime(arr):

    # a very simple function to check a number is prime or not
    def checkPrime(number):
        for i in range(2, int(number/2)):
            if number % i == 0:
                return False
        return True

    primeNumbers = filter(lambda x: checkPrime(x), arr)
    return map(lambda x: square(x), primeNumbers)

# we can not access checkPrime from here
# checkPrime(5)

result = filterAndSquarePrime(array)
list(result)

# Importing Modules
# import module 'math' to uses functions for calculating
import math

# print the square root of 16
print(math.sqrt(16))

# we can create alias when import a module
import numpy as np

print(np.sqrt(16))

# Import Certain functions from Modules
# only import function 'sin' in package 'math'
from math import sin

# use the function
print(sin(60))
