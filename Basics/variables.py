# Initiate variables first
x = 5
y = "john"
str_var = str(3)
int_var = int(3)
float_var = float(8)

# Print variables
print(x) # 5 as number
print(y) # john as string
print(str_var) # 3 as string
print(int_var) # 3 as number
print(float_var) # 8 as decimal

# show the data type
print(type(y)) 
print(type(int_var))
print(type(float_var))

# multiple variables initied
a, b, c = 'orange', 5, float(9)
fruits = ['apple', 5]
print(a) # multiple variables
print(fruits)

# Printing more than one value
# Can not concatenate a string and integer
print(a + y)
print(a, y)

# Adding two intergr
print(x + int_var)

global_var = "9"

def myFunc():
    print('Global value ' + global_var)

myFunc()

#  use the global keyword
def mySecondfunc():
  global global_var_second
  global_var_second = "fantastic"

mySecondfunc()

print("Python is " + global_var_second)

#  use the global keyword if you want to change a global variable inside a function.
global_var_third = "awesome"

def myThirdfunc():
  global global_var_third
  global_var_third = "fantastic"

myThirdfunc()

print("Python is " + global_var_third)