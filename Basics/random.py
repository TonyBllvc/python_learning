import random


# Print random numbers, between 1 and 9
print(random.randrange(1, 10))

#print a random number:
print(random.random())

#capture the state:
state = random.getstate()

#print another random number:
print(random.random())

#restore the state:
random.setstate(state)

#and the next random number should be the same as when you captured the state:
print(random.random())