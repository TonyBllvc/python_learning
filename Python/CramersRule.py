
# Prompt the user to enter the coefficients of 'a' to 'f'
a, b, c, d, e, f = eval(input("Enter the coefficients of 'a' to 'f' respectively - seperated by commas: "))

# Compute ad - bc
check = a*d - b*c

#Check if ad - bc != 0 and print results
if check == 0:
    print ("The equation has no solution")
    
else:
    x = (e*d - b*f)/(a*d - b*c)
    y = (a*f - e*c)/(a*d - b*c)
    print (f"x is {x} and y is {y}")