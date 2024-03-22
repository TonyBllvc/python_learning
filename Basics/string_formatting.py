# Python String Formatting

# To make sure a string will display as expected, we can format the result with..
# .. the format() method.

# String format()
# The format() method allows you to format selected parts of a string.

# Sometimes there are parts of a text that you do not control, maybe they come..
# .. from a database, or user input?

# Definition and Usage
# The format() method formats the specified value(s) and insert them inside the string's placeholder.

# The placeholder is defined using curly brackets: {}.
# :<		Left aligns the result (within the available space)
# :>		Right aligns the result (within the available space)
# :^		Center aligns the result (within the available space)
# :=		Places the sign to the left most position
# :+		Use a plus sign to indicate if the result is positive or negative
# :-		Use a minus sign for negative values only
# : 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
# :,		Use a comma as a thousand separator
# :_		Use a underscore as a thousand separator
# :b		Binary format
# :c		Converts the value into the corresponding unicode character
# :d		Decimal format
# :e		Scientific format, with a lower case e
# :E		Scientific format, with an upper case E
# :f		Fix point number format
# :F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g		General format
# :G		General format (using a upper case E for scientific notations)
# :o		Octal format
# :x		Hex format, lower case
# :X		Hex format, upper case
# :n		Number format
# :%		Percentage format

# p = "iwo {:>}".format(34)


txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36) # Named Indexes
txt2 = "My name is {0}, I'm {1}".format("John",36) #Index Numbers
txt3 = "My name is {}, I'm {}".format("John",36) # Multiple Values

# print(p)
print(txt1)
print(txt2)
print(txt3)
# The format() method returns the formatted string.

# To control such values, add placeholders (curly brackets {}) in the text,..
#  .. and run the values through the format() method:
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

quantity = 3
itemno = 567
prices = 49
myorders = "I want {} pieces of item number {} for {:.2f} dollars."
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorders.format(quantity, itemno, price))
print(myorder.format(quantity, itemno, prices))


txts = "For only {price:.2f} dollars!"
print(txts.format(price = 49))