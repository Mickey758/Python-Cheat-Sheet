# This cheat sheet was made by MickeyYe#0001, id: 847917077641953340
# >> Output
# This cheat sheet was made for python version 3.9 >

# --------------------
# Variables
# --------------------
my_variable = "value" # String
my_variable = 69 # Integer
my_variable = 69.9 # Float
my_variable = [] # Array
my_variable = {} # Dictionary
my_variable = () # List
my_variable = True # Boolean

# --------------------
# Prining to the console
# --------------------
print("Hello World!") >> "Hello World!"

# You may also print variables

my_variable = "Hello"
print(my_variable) >> "Hello"

my_variable = 12
print(my_variable) >> 12

my_first_variable = "Hello"
my_second_variable = "World!"
print(my_first_variable,my_second_variable) >> "Hello World!" # Using commas after variables will input a space
print(my_first_variable+my_second_variable) >> "HelloWorld!" # Using a plus, will put the two strings together

my_first_variable = "I am"
my_second_variable = 16
my_third_variable = "years old"
print(my_first_variable,my_second_variable,my_third_variable) >> "I am 16 years old"


# --------------------
# F Strings
# --------------------
# F strings allow you to input variables while in duoble quotes or apostophes
# To make a "f string", you need to input a f or F before the double quotes or apostrophe 
my_first_variable = "Mickey"
print(f"My name is {my_first_variable}") >> "My name is Mickey"

my_first_variable = "John"
print(F"My friend's name is {my_first_variable}") >> "My friend's name is John"


# --------------------
# Functions
# --------------------
def greeting():
    print("Hello World")
greeting()              >> "Hello World"

# You can also have arguments in a function
def grerting(text):
    print(text)
greeting("Hello There")  >> "Hello There"

# You can make function arguments default to something if no argument was provided
def greeting(text="Hi!"):
    print(text)
greeting()       >> "Hi"


# --------------------
# Math operators
# --------------------
# (+) = Addition
1 + 1 >> 2

# (-) = Subtraction
3 - 2 >> 1

# (*) = Multiplication
5 * 5 >> 25

# (/) = Division
10 / 5 >> 2.0

# (%) = Modulas
15 % 10 >> 5

# (**) = Exponent
2 ** 10 >> 1024

# (//) = Floor division
11 // 3 >> 3

# (+=) Add and assign the result
my_variable = 2
my_variable += 1
print(my_variable) >> 3

# (-=) Subtract and assign the result
my_variable = 4
my_variable -= 2
print(my_variable) >> 2

# (*=) Mutliply and assign the result
my_variable = 5
my_variable *= 5
print(my_variable) >> 25

# (/=) Divide and assign the result
my_variable = 6
my_variable /= 2
print(my_variable) >> 3.0

# (%=) Find the modulas and assign the result
my_variable = 15
my_variable %= 5
print(my_variable) >> 5

# (**=) Find the exponent and assign the result
my_variable = 2
my_variable **= 10
print(my_variable) >> 1024

# (//=) Find the floor division and assign the result
my_variable = 11
my_variable //= 3
print(my_variable) >> 3


# --------------------
# Comparison Operators
# --------------------
# (==) = equal to
1 == 2 >> False

# (!=) = not equal to
2 != 2 >> False

# (>) = Greater than
3 > 1 >> True

# (<) = less than
5 < 10 >> True

# (>=) = greater than or equal to
5 >= 2 >> True
4 >= 4 >> True
7 >= 8 >> False

# (<=) = less than or equal to
3 <= 2 >> False
6 <= 6 >> True
2 <= 5 >> True


# --------------------
# If, elif and else gates
# --------------------
# As we learned before, 1 == 2 results in False. As this is False, the gate will look for another condition, example
if 1 == 2:
    print("They are equal") # If the condition was True, then it would print this
else:
    print("They are not equal") # >> This will be th output as 1 is not equal to 2
    
# You can also do this with variables
a = 2
b = 2
if a == b:
    print("They are equal") # >> This will be the output as a and b are the same
else:
    print("They are not equal") # 2 is equal to 2 so it will go the first confition

# This is the same for all the comparison operators found on line 130

# --------------------
# Logical Operators
# --------------------
# (and) if two conditions are true
a = 2
b = 3
if a == 2 and b == 3:
    print("All conditions were met") # >> This will be the output as all the conditons meet
else:
    print("Not all of the conditions were met")
    
# (or) if one condition is true
a = 5
b = 6
if a > b or b > a:
    print("One or more conditions were met") # This will be the output as one or more of the conditions meet
else:
    print("No conditions met")

#---------------------------
# While loops 
#--------------------------

washing = True # setting washing to true
while washing:  # basically saying while washing is equal to True it should continuously do a task until it is false 
    print("hello") # this would print hello continuously until washing is false or until the program is stopped
    washing = False # this is a way you can break the loop
# another way of writing this 

while True: # this is saying whilse something is true it should do something until it is false 
    print("hello") # this would print hello until the while loop turns false or the program is closed
    break # this is another way to break the loop as well

while 1:
    print("hello") # this is the same this as saying while True but the number 1 is equal to 
    
# you can apply the same concept to false as well

# you can also use while loops for math equations as well

a = 6 # setting the variable a equal to 6 
while a == 6: # this is saying while variable a is equal to 6 you want it to do something until the value changes or the loop is broken
    print("hello") # hello will be printed until the loop is broken
    a = 7 # this is one way of breaking the loop in while loop math equations

#-------------------------
# For loops
#-------------------------

a = 50 # setting variable a equal to 50 
for i in range(a): # this is saying for each number in variable a you want to do something for the amount stated
    print("hey") # it would print hey 50 times

# another way of writing this 

for i in range(50): # instead of setting a variable you can do it straight forward it basically does the same thing, for each number in 50 it would do something for that amount
    print("hey") # this would print hey 50 times

