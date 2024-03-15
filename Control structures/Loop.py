#Loops
words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1

while counter <= max_index:
    word = words[counter]
    print(word + "!")
    counter = counter + 1

#for loops
words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")

#for loops
for i in range(5):
    print("hello!")

#eg
for i in range(0, 20, 2):
    print("i")

#eg
i = 3
while i >= 0:
    print(i)
    i = i - 1

#while 1 == 1:
 #   print("In the loop")

 #eg
# x = 0
 #while x <= 20:
  #   print(x)
   #  x += 2

#eg
i = 5
while True:
    print(i)
    i = i - 1
    if i <= 2:
        break

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