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