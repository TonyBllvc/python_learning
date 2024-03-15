# Import Random integers from Random Library
from random import randint

# Generate three ramdom numbers
number1 = randint(0, 100)
number2 = randint(0, 100)

# Prompt the user for the sum of the randomly generated numbers
answer = eval(input(f"What is {number1} + {number2}: "))

# Display result
print (f"Your answer is",number1 + number2 == answer)