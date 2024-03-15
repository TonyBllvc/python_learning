from array import *
#this is array containing type double
a = array('d', (2.1, 2.3, 5.6, 4.3, 3.5))
b = array('d', (4.1, 4.3, 3.6))
a.append(3.9) #appending operation
b.extend([3.4, 3.2, 3.0]) #Extending array b with the values
c = array('i', (1,2,3,4,5,7))
c.insert(5,6)
#Next we print the operation
print(a)
print(b)
print(c)