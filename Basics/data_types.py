
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


# Example	Data Type
a = "Hello World"	# str	
b = 20	#int	
c = 20.5	#float	
d = 1j	#complex	
f = ["apple", "banana", "cherry"]	# list	
g = ("apple", "banana", "cherry")	# tuple	
h = range(6)	# range	
i = {"name" : "John", "age" : 36}	# dict	
j = {"apple", "banana", "cherry"}	# set	
k = frozenset({"apple", "banana", "cherry"})	# frozenset	
l = True	# bool	
m = b"Hello"	# bytes	
x = bytearray(5)	# bytearray	
y = memoryview(bytes(5))	# memoryview	
z = None	# NoneType


print(a)
print(b)
print(c)
print(d)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)
print(x)
print(y)
print(z)

x_a = str("Hello World")	# str	
x_b = int(20)	# int	
x_c = float(20.5)	#float	
x_d = complex(1+8j)	# complex	
x_f = list(("apple", "banana", "cherry"))	# list	
x_g = tuple(("apple", "banana", "cherry"))	# tuple	
x_h = range(6)	# range	
x_i = dict(name="John", age=36)	# dict	
x_j = set(("apple", "banana", "cherry"))	# set	
x_l = frozenset(("apple", "banana", "cherry"))	# frozenset	
x_m = bool(5)	# bool	
x_n = bytes(5)	# bytes	
x_o = bytearray(5)	# bytearray	
x_p = memoryview(bytes(5))	# memoryview

print(x_a)
print(x_b)
print(x_c)
print(x_d)
print(x_f)
print(x_g)
print(x_h)
print(x_i)
print(x_j)
print(x_l)
print(x_m)
print(x_n)
print(x_o)
print(x_p)

# Convert from one type to another:
# Note: You cannot convert complex numbers into another number type.
x_int = 1    # int
y_float = 2.8  # float
z_complex = 1j   # complex

#convert from int to float:
a_float = float(x_int)

#convert from float to int:
b_int = int(y_float )

#convert from int to complex:
c_complex = complex(x_int)

print(a_float)
print(b_int)

print(c_complex)

print(type(a_float))
print(type(b_int))
print(type(c_complex))
