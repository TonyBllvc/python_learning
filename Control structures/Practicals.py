x = 5
y = 6
if x > y:
    print("True")
else:
    print("False")

#Range
lists = range(10)
print(lists)

#
numbers = list(range(10))
print(numbers[4])

#eg
nums = list(range(5, 8))
print(nums)

print(range(20) == range(0, 20))

#eg
letters = ['a', 'b', 'c']
for i in letters:
    print(i)

#This
words = range(5)
for i in words:
    print("hello!")

#Or
for i in range(5):
    print("Hello!")

#again
for i in range(0, 20, 2):
    print(i)

#test
list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])

#eg
for i in range(10):
    if not i % 2 == 0:
        print(i)

#or
#eg
for i in range(10):
    if not i % 2 == 0:
        print(i+1)

#eg
while False:
    print("Looping...")

#eg
list = [1, 2, 3, 4]
if len(list) % 2 == 0:
    print(list[0])

#eg
list = [1, 2, 3]
for var in list:
    print(var)

#eg 
words = ["I", "am", "happy"]
for word in words:
    print(word + "!")

#eg
def square(x):
    return x * x

def test(func, x):
    print(func(x))

test(square, 42)

import random

for i in range(5):
    value = random.randint(1, 6)
    print(value)

#eg
#ef sum(x):
#    res = 0
#for i in range(x):
#   res += i
#return res

#print(sum(5))

#dictionary
pairs = [1, 2, 3, 4, 112, 123]
if 112 in pairs:
    print("True!")
elif not 112 in pairs:
    print("False!")
else:
    print("None!")