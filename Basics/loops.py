# Python Loops
# Python has two primitive loop commands:

# while loops
# for loops


# _____ while loops ___________________

# Print i as long as i is less than 6:
i = 1

while i < 6: # Note: remember to increment i, or else the loop will continue forever.
  print(i)
  i += 1


# The break Statement
k = 1
while k < 6:
  print(k)
  if k == 3:
    break
  k += 1

# The continue Statement
#   With the continue statement we can stop the current iteration, and continue with the next:
j = 0
while j < 6:
  j += 1
  if j == 3:
    continue
  print(j)

# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")



# _____ for loops ___________________
#   Python For Loops
fruites = ["apple", "banana", "cherry"]
for x in fruites:
  print(x)

# Looping Through a String
for y in "banana":
  print(y)

# The break Statement
fruit = ["apple", "banana", "cherry"]
for z in fruit:
  print(x)
  if x == "banana":
    break
  
fruities = ["apple", "banana", "cherry"]
for u in fruities:
  if u == "banana":
    break
  print(u)

# The continue Statement
fruitCherry = ["apple", "banana", "cherry"]
for q in fruitCherry:
  if q == "banana":
    continue
  print(q)

#  Pyrhon for the range() Function
for o in range(6):
  print(o)

for f in range(2, 6):
  print(f)

for t in range(2, 30, 3): #To increnent the eange of values by 3
  print(t)

# Else in For Loop
for d in range(6):
  print(d)
else:
  print("Finally finished!") 

for n in range(6):
  if n == 3: break
  print(n)
else:
  print("Finally finished!")

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for s in adj:
  for t in fruits:
    print(s, t)

# The pass Statement
for x in [0, 1, 2]:
  pass