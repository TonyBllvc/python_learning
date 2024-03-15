#Exception handling
try:
    num1 = 7
    num2 = 0
    print (num1 / num2)
    print ("Done calculation")
except ZeroDivisionError:
    print("An error occured")
    print("due to zero division")

#eg
#meaning = 42
#print(meaning / 0)
#print("the meaning of life")
#except (ValueError, TypeError):
#    print("ValueError or TypeError occured")
#except ZeroDivisionError:
#    print("Divided by zero")


#eg
#try:
#    word = "spam"
#    print(word / 0)
#except:
#    print("An error occureds")

#eg
try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Divide by zero")
finally:
    print("This code will run no matter what")

#eg
try:
    num1 = input(":")
    num2 = input(":")
    print(float(num1) / float(num2))
except:
    print("Invalid code")

#raising execptions
name = "123"
raise NameError("Invalid name!")

#raising exception
print(1)
raise ValueError
print(2)

#eg
try:
    print(1 / 0)
except ZeroDivisionError:


    raise ValueError



#eg
#print(1/0)
#except ZeroDivisionError:
#    raise ValueError

#eg
num = input(":")
if float(num) < 0:
    raise ValueError("Negative!")
