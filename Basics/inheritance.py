# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties..
# ..from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

# ************* starts *************
# Create a Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# Now
# Create a Child Class
# To create a class that inherits the functionality from another class,..
#  ..send the parent class as a parameter when creating the child class:
class Student(Person):
  pass

# Note: Use the 'pass' keyword when you do not want to add any other..
#  .. properties or methods to the class.

# Now the Student class has the same properties and methods as the Person class.

y = Student("Mike", "Olsen")
y.printname()

# ************* ends *************

# Complete code unction for inheriance

# Python also has a super() function that will make the child class..
#  ..inherit all the methods and properties from its parent:

# By using the super() function, you do not have to use the name of the..
#  ..parent element, it will automatically inherit the methods and properties..
#  ..from its parent.

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

a = Student("Mike", "Olsen", 2019)
a.welcome()
