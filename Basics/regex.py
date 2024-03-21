# Python RegEx
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.

# Import the re module:
import re

txts = "The rain in Spain"
y = re.search("^The.*Spain$", txts)

print(y)

# The findall() Function
# The findall() function returns a list containing all matches.

txtl = "The rain in Spain"
xl = re.findall("ai", txtl)
print(xl)




txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
# ...This work is not complete, everything is online