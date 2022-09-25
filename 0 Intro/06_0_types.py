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

print(type(my_function))   # function
print(type(my_function())) # str




# Show converting string from input to int