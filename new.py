import math

# Show me everything inside 'math'
print(dir(math))

# Check what 'pi' is
print(type(math.pi))     
# Output: <class 'float'> (It's just a number)

# Check what 'sqrt' is
print(type(math.sqrt))   
# Output: <class 'builtin_function_or_method'> (It's an action/tool)

# Read the manual for the power function in the math module
help(math.pow)
# Read the manual for the math module
# help(math)

# Apply:
radius = 5
area = math.pi * math.pow(radius, 2)
print(f"The area is: {area}")