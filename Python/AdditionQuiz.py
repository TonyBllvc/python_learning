
# Import Random integers from Random Library
import random

# Generate three ramdom numbers
number1 = random.randint(0, 20)
number2 = random.randint(0, 20)
number3 = random.randint(0, 20)

# Prompt the user for the sum of the randomly generated numbers
answer = eval(input(f"What is {number1} + {number2} + {number3}: "))

# Display result
print (f"{number1} + {number2} + {number3} is = {answer} is",number1 + number2 + number3 == answer)