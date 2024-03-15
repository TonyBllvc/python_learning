#Function
def my_func():
    print("spam")
    print("spam")
    print("spam")

my_func()

#Functions with argument
def my_func():
    print("Hi!")

my_func()

def print_with_exclamation(word):
    print(word + "!")

print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")

#eg
def print_double(x):
    print(2 * x)

print_double(3)

#Functions with more than one argument
def print_sum_twice(x, y):
    print(x + y)
    print(x * y)

print_sum_twice(3, 5)

#eg
def even(x):
    if x%2 == 0:
        print("Yes!")
    else:
        print("No!")

even(2)

#Returning from functions
#def max(x, y):
 #   if x >= y:
  #      return x
   # else:
    #    return y
    
  #  print(max(4, 7))
   # z = max(8, 5)
    #print(z)
    
#eg
#def add_number(x, y):
#    if len(x) >= len(y):
#        return x
#    else:
#       return y

#add_number(3, 7)

#Returning from Functions
def add_number(x, y):
    total = x + y
    return total
    print("This won't be printed")

print(add_number(4, 5))

#def print_numbers():
#    print(1)
#    print(2)
#    return
#    print(4)
#    print(6)

#Comments & Docstrings
#eg
x = 365
y = 7
# this is a comment

print(x % y) # find the reminder
#print (x // y)
#print another comment

#or 
def module_num(x, y): #setting the variables
    print(x % y) #finding the reminder
#print the reminder
module_num(365, 7) #assigning the variables with int

#Docstring
def shout(word):
    """
    print a word with an exclaimation mark following it
    """
    print(word + "!")

shout("spam")

#Functions
def multiply(x,y):
    return x * y

a = 4
b = 7
operation = multiply
print(operation(a, b))


# function
def add(x, y):
    return x + y

def do_twice(func, x, y):
    return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))
"""
come back
"""

#Modules 
import random

for i in range(6):
    value = random.randint(1, 6)
    print(value)

#eg
import math
num = 16
print(math.sqrt(num))

#To Import Pie
from math import pi

print(pi)

