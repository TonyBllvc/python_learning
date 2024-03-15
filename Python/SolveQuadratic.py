# Import the math library
import math

# Prompt the user to enter the values for a, b, and c
a, b, c = eval(input("Enter the values for a, b, and c respectively - seperated by commas: "))

# Compute the discriminant
discriminant = b**2 - 4*a*c

# Check if the discriminant is positive, negative, or zero and print result
if discriminant > 0:
    root1 = (- b + math.sqrt (b**2 - 4*a*c)) / 2*a
    root2 = (- b - math.sqrt (b**2 - 4*a*c)) / 2*a
    print (f"The roots are {root1} and {root2}")
    
elif discriminant == 0:
    root = (- b + math.sqrt (b**2 - 4*a*c) / 2*a)
    print (f"The root is {root}")

else:
    print ("The equation has no real roots")