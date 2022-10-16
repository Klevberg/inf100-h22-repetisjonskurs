# Methods in Python are tools that you can use on data
# Different data types have different built-in methods
# For example, you can find the
# We will start by looking at string methods

# String methods: https://www.w3schools.com/python/python_strings_methods.asp


s = "aB cd"

print(s)


# The .capitalize() method capitalizes the first letter of a string

print(s.capitalize())


# Strings are not mutable, which means if we want to change a string,
# we must reassign a value to the variable.
# Notice that s remains unchanged even though we used the .capitalize() method

print(s)


# The .upper() method turns all the letters of a string into uppercase letters

s = s.upper() # Here, variable 's' is assigned a new value
print(s)


# The .lower() method turns all the letters of a string into lowercase letters

s = s.lower()
print(s)


# The .replace() method replaces a substring of a string with another string

s = "INF101"
print(s.replace("101", "100"))


# The .count() method counts the number of a certain character in a string

print(s.count('1'))


# The .index() finds the index of a certain character in a string
# If this character can be found multiple times in the string,
# the method will return the index of the first case

print(s.index('1'))


# To demonstrate the next method, we start by looking at a string with
# whitespace on both sides

s = '  hello    \n'
print(s)
print(repr(s))
print(len(s))
print()

# The .strip() method removes any whitespace on either side of the string

s = s.strip()
print(s)
print(repr(s))
print(len(s))


# Let's look at .split() and .join()

# The .split() method splits a string into a list

sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
words = sentence.split()
print(words)

# We can specify a separator. By default, the separator is any whitespace

new_list = sentence.split('o')
print(new_list)


# The .join() method is used to turn a list of strings into a single string

print(" ".join(words))

# Inside the string, we specify what we want to put inbetween each string

print("o".join(new_list))
