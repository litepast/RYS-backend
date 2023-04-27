# Define some functions
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def double(x):
    return x * 2

# Create a list of functions
functions = [square, cube, double]

# Apply each function to a value and print the result
value = 3
for func in functions:
    result = func(value)
    print(result)

