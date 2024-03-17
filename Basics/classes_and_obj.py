# Python Classes/Objects

# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

# The __init__() Function

# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in __init__() function.

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary..
#  .. to do when the object is being created:

# example:
# Create a class named Person, use the __init__() function to assign values for name and age:
class PersonOne:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = PersonOne("John", 36)

print('init')
print(p1.name)
print(p1.age)

# Note: The __init__() function is called automatically every time the class is ..
#  .. being used to create a new object.



# The __str__() Function
# The __str__() function controls what should be returned when the..
#  .. class object is represented as a string.

# If the __str__() function is not set, the string representation of the object is returned:

# Example
# The string representation of an object WITHOUT the __str__() function:

class PersonTwo:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = PersonTwo("John", 36)

print('str')
print(p1.name)

# ********************* ^^ **********************
class PersonThree:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = PersonThree("John", 36)

print('a')
print(p1)

# *************** start **************************************
# Object Methods

# Objects can also contain methods. Methods in objects are functions that belong to the object.

# Let us create a method in the Person class:
class PersonFour:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfuncFour(self):
    print("Hello my name is " + self.name)

print('al')
p1 = PersonFour("John", 36)
# p1.name = "40"
p1.myfuncFour()
# Note: The self parameter is a reference to the current instance of the class, and..
# ..is used to access variables that belong to the class.

# It does not have to be named "self" , you can call it whatever you like,..
# ..but it has to be the first parameter of any function in the class:
# *********************** end *******************************

# Modify Object Properties
# You can modify properties on objects like this:
p1.age = 40


# Delete Object Properties
# You can delete properties on objects by using the del keyword:
del p1.age

# Delete Objects
# You can delete objects by using the del keyword:
del p1

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition..
#  .. with no content, put in the pass statement to avoid getting an error.
class Person:
  pass