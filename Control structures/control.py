#if statement
num = 12
if num > 5:
    print("Bigger than 5")
    if num <= 47:
        print("Between 5 and 47")

#else statement
x = 4
if x == 5:
    print("Yes")
else:
    print("No") 

num = 7
if num == 5:
    print("Number is 5")
else:
    if num == 11:
        print("Number is 11")
    else:
        if num == 7:
            print("Number is 7")
        else:
            print("Number isn's 5, 11 or 7")  

#elseif statement
num = 7
if num == 5:
    print("Number is 5")
elif num == 11:
    print("Number is 11")
elif num == 7:
    print("Number is 7")
else:
    print("Number isn't 5, 11 or 7")
        
#Boolean logic. 
# And
#>>> 1 == 1 and 2 == 2
#True
#>>> 1 == 1 and 2 == 2
#false
#>>> 1 != 1 and 2 == 2
#>>> 2 < 1 and 3 > 6
#false

if 1 == 1 and (2 + 2 > 3):
    print("True")
else:
    print("False")

#Boolean Or
#>>> 1 == 1 or 2 == 2
#True
#>>> 1 == 1 or 2 == 3
#True
#>>> 1 != 1 or  2 == 2
#True
#>>> 2 < 1 or 3 > 6
#False

if 1 != 2 or 3 > 5:
    print("True")
else:
    print("False")

#Boolean Not
#>>> not 1 == 1
#False
#>>> not 1 > 7
#True

if not 1 == 1:
    print("True")
else:
    print("False")

if not True:
    print("1")
elif not (1 + 1 == 3):
    print("2")
else:
    print("3")

#Operator Precedence
#>>> False == Fals or True
#True
#>>> False == (False or True)
#False
#>>>(False == False) or True
#True
#Note: Python's order is the same as that of mathematical operations

#eg of operation precedence
if 1 + 1 * 3 == 6:
    print("Yes")
else:
    print("No")

#While Loops
i = 1
while i <= 5:
    print(i)
    i = i + 1

print("Finished!")

#eg
i = 3
while i >= 0:
    print(i)
    i = i - 1

print("Finished!")

#While Loop - Infinite loop
#while 1 == 1:
 #   print("In the loop")

#Class Work
x = 0
while x <= 20:
    print(x)
    x += 2

#Break loop
i = 0
while 1 == 1:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break
print("Finished")
    
#Example
i = 5
while True:
    print(i)
    i = i - 1
    if i <= 2:
        break

#continue
i = 0
while True:
    i = i + 1
    if i == 2:
        print("Skipping 2")
        continue
    if i == 5:
        print("Breaking")
        break
    print(i)

print("Finished!")

#Lists
words = ["Grape", "Watermelon", "Orange"]
print(words[0])
print(words[1])
print(words[2])

#Lists - Empty
empty_list = []
print(empty_list)

number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
#print(things[2][2])

#lists-strings
str = "Hello world!"
print(str[6])