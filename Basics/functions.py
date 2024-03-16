def my_functionFirst():
  print("Hello from a function")

my_functionFirst()

#  Atguments
def my_functionSecond(fname):
  print(fname + " Refsnes")

my_functionSecond("Emil")
my_functionSecond("Tobias")
my_functionSecond("Linus")

def my_functionThird(fname, lname):
  print(fname + " " + lname)

my_functionThird("Emil", "Refsnes")

# Arbitrary Arguments, *args
# If the number of arguments is unknown, add a * before the parameter name:
# This way the function will receive a tuple of arguments, and can access the 
# items accordingly:
def my_functionFourth(*kids):
  print("The youngest child is " + kids[2])

my_functionFourth("Emil", "Tobias", "Linus")

# Keyword Arguments
def my_functionFifth(child3, child2, child1):
  print("The youngest child is " + child3)

my_functionFifth(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs 

# If you do not know how many keyword arguments that will be passed into your function, add
#  two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and 
# can access the items accordingly:
def my_functionSix(**kid):
  print("His last name is " + kid["lname"])

my_functionSix(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value

# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:
def my_functionSeven(country = "Norway"):
  print("I am from " + country)

my_functionSeven("Sweden")
my_functionSeven("India")
my_functionSeven()
my_functionSeven("Brazil")


# Passing a List as an Argument

# You can send any data types of argument to a function (string, number, list, dictionary etc.),..
# .. and it will be treated as the same data type inside the function./
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass Statement

# function definitions cannot be empty, but if you for some reason have a function..
#  ..definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass


# Positional-Only Arguments

# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:
def my_function(x, /):

  print(x)

my_function(3)

# Also
# Without the , / you are actually allowed to use keyword arguments even..
#  .. if the function expects positional arguments:
def my_function(x):
  print(x)

my_function(x = 3)

# Keyword-Only Arguments

# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, x):
  print(x)

my_function(x = 3)

# Also
# Without the *, you are allowed to use positionale arguments even if the function..
# .. expects keyword arguments:
def my_function(x):
  print(x)

my_function(3)

# Combine Positional-Only and Keyword-Only

# You can combine the two argument types in the same function.
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

# Recursion

# Python also accepts function recursion, which means a defined function can call itself.

# Recursion is a common mathematical and programming concept. It means that a function calls..
#  ..itself. This has the benefit of meaning that you can loop through data to reach a result.

# The developer should be very careful with recursion as it can be quite easy to slip into writing..
#  ..a function which never terminates, or one that uses excess amounts of memory or processor..
# ..power. However, when written correctly recursion can be a very efficient and..
#  ..mathematically-elegant approach to programming.

# In this example, tri_recursion() is a function that we have defined to call itself ("recurse")...
# .. We use the k variable as the data, which decrements (-1) every time we recurse. The recursion..
#  ..ends when the condition is not greater than 0 (i.e. when it is 0).

# To a new developer it can take some time to work out how exactly this works, best way to find..
# ..out is by testing and modifying it.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(7)

# Python Lambda

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
x = lambda a : a + 10
print("lambda")
print(x(5))

# Or
y = lambda a, b, c : a + b + c
print("lambda two")
print(y(5, 6, 2))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be.. 
# ..multiplied with an unknown number:
def myfuncTwo(n):
  return lambda a : a * n

mydoubler = myfuncTwo(2)

print('Lambda functions')
print(mydoubler(11))

# Or, use the same function definition to make both functions, in the same program:
def myfuncAll(n):
  return lambda a : a * n

mydouble = myfuncAll(2)
mytriple = myfuncAll(3)

print('Both')
print(mydouble(11))
print(mytriple(11))

# Use lambda functions when an anonymous function is required for a short period of time.