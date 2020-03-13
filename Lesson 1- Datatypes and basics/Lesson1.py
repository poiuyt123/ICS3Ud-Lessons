# Data-types 

#Words, characters, cannot be operated on, can only be concatenated.
word = "I am a string" # string, strings are always inside of quotes

# Numbers - Can be operated on (+, -, *, /, %) % is called "modulo"
number = 5             # Integer, for whole number
number_2 = 7.5         # Float


# Bool - only yes or no
switch = True          # Boolean, true or false

# operation properties
quotient = number / number_2 # Datatype ?? Float
quotient2 = 4 / 2 # Datatype ?? float by default

# // gives integer division, i.e. the decimal is dropped
quotient3 = 5 // 2 # Datatype ?? float

# conversions
intConvert = int(4.9)  # int() converts to integer, ALWAYS ROUNDS DOWN

#Concatenation - combining two strings together
stringA = "hello"
stringB = "world"

concatString = stringA + " " + stringB


print(concatString)