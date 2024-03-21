# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.

import platform

x = platform.system()
print(x)

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

# Example
# List all the defined names belonging to the platform module:
x = dir(platform)
print(x)

# Note: The dir() function can be used on all modules, also the ones you create yourself.