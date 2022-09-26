"""
Built-in functions are tools we can use when programming in Python

Some that we have already seen:
print(), input(), len(), type()

The following are functions for converting / casting values from one type to another:
str(), int(), float(), bool(), list()

We have some nice functions for working with math:
abs(), max(), min(), round(), sum()

Some that will come handy when using loops:
range(), enumerate()

And many more!
See here for a list: https://docs.python.org/3/library/functions.html
"""

"""
Built-in functions will often take several arguments (values that are sent in to a function's parameters).
Instead of giving a value for every field in the same order, we can specify what argument we want to use.
For example, the function print() has multiple arguments.
One of them is called 'end'. It lets us choose what happens when the print() function has finished printing a line.
We use it like this: print("let's hope for no rain", end=' ')
"""

# The default value is '\n' (newline)
print("let's hope for no rain")

# We can replace the newline with a space like this
print("let's hope for no rain", end=' ')

# Now the next time we print, it will start from the same line
print("today")
