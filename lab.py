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
