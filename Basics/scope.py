# A variable is only available from inside the region it is created. This is called scope.

# Local Scope

# A variable created inside a function belongs to the local scope of that function, and can..
# .. only be used inside that function.
def myfuncFirst():
  x = 300
  print(x)

myfuncFirst()

# Function Inside Function
# As explained in the example above, the variable x is not available outside the function, but..
# .. it is available for any function inside the function:
def myfuncSecond():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfuncSecond()

# Naming Variables
# If you operate with the same variable name inside and outside of a function, Python will treat them..
#  as two separate variables, one available in the global scope (outside the function) and one..
# .. available in the local scope (inside the function):
x = 300

def myfuncThird():
  x = 200
  print(x)

myfuncThird()

print(x)

# Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

# The global keyword makes the variable global.
def myfuncFour():
  global x
  x = 300

myfuncFour()

print(x)

# Also, use the global keyword if you want to make a change to a global variable inside a function.
# ...