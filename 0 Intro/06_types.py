# The following types are essential within Python

# Int, float, bool, string, list, tuple, None
print(type(3))          # int      (whole number)
print(type(1.23))       # float    (decimal number)
print(type(4 < 5.2))    # bool     (boolean value, True or False)
print(type("hi"))       # str      (string / text)
print(type([1, 2, 3]))  # list
print(type((1, 2, 3)))  # tuple
print(type(None))       # NoneType (even "nothing" has a type)

# Later in the course we will look at set and dict
print(type({1, 5}))             # set
print(type({'key': 'value'}))   # dict

# Functions also have their own type
def my_function():
    return "hello"

print(type(my_function))    # function
print(type(my_function()))  # str
print(type(print("Hello"))) # NoneType


# Let's take a look at how we can solve the problem from earlier
a = input("Number A: ")
b = input("Number B: ")

# Variable a and b are strings, so they are put together
print("The sum is", a + b)

# We convert the strings a and b to type int (integer / whole number)
a = int(a)
b = int(b)
print("The sum is", a + b)
