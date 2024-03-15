# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print('a is greater than b')
  
# or
if a > b: print("a is greater than b") 

# Short Hand If ... Else
# Ternary Operators, or Conditional Expressions.
A = 2
B = 330
print("A") if A > B else print("B")

x = 330
y = 330
print("A") if x > y else print("=") if x == y else print("B")

# And
j = 200
l = 33
m = 500
if j > l and m > j:
  print("Both conditions are True")

  
# Or
j = 200
l = 33
m = 500
if j > l or j > j:
  print("Both conditions are True")

# Not
p = 33
q = 200
if not p > q:
  print("a is NOT greater than b")

# Nested If
g = 41

if g > 10:
  print("Above ten,")
  if g > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# The pass Statement
# if statements cannot be empty, but if you for some reason have an...
# ... if statement with no content, put in the pass statement to avoid getting  ...
# .. an error.
    
u = 33
w = 200

if u > w :
  pass