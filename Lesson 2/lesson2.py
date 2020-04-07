import math


# Inputs

#NOTE: the value collected by input, will always be a string.

length = input("provide the length of your property in meters: ")
width = input("provide the width of your property in meters: ")

length = int(length)
width = int(width)

area = length * width
area = str(area)

# # concatenation example
print("Your area is: " + area + " meters squared")

# Quick intro to importing libraries and using their functions
toRoot = input("Please enter a number to find its root: ")
toRoot = int(toRoot)
root = math.sqrt(toRoot)

print("the root is: " + str(root))

## BOOLEAN EXPRESSIONS and Operators
# Three Boolean Operators: and, OR, !(not)
on = True
off = False

# AND operator: return True if both arguments on each side are true. Otherwise, returns false
andExample = on and off

# OR operator: checks if either of the sides is true. If one or both are true, it will return true
orExample = on or off

# NOT (!) operator: 
notExample = not on

# Order of Boolean Operations: NOT, then AND, then OR
combinedExample = not on or off and on

print(combinedExample)

