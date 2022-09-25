# We can store a string in a variable. This allows us to use it later
message = "I'm a string"
message += "!!!"

print(message)


# We can store integers (whole numbers) in the same way
number_1 = 10
number_2 = 20

theSum = number_1 + number_2

print(theSum)


# The symbol '=' here means that we assign the value 5 to the variable x
x = 5
print(x)     # 5
print(2 * x) # 10
print(x)     # still 5

x = x * 2
print(x)


# As shown above, in contrast to a variable in math, a variable in Python can be changed
y = 10      # The variable y is given the value 10
print(y)    # 10

y = True    # The variable y now refers to the value True
y = "Hi"    # The variable y now refers to the value "Hi"
y = 3       # The variable y now refers to the value 3
y = y + 1   # The variable y now refers to the value 4
print(y)    # 4
print(y)    # still 4


# Naming conventions

# 1. Variable names must start with a letter
# 2. Use _ between words
    # Good: first_name = "Ola"
    # Meh:  firstName = "Ola"
# 3. Use lower case letters for most variables
    # Good: name = "Ola"
    # Bad:  Name = "Ola"
# 4. Use upper case letters for constants (variables with values that never change)
    # Good: PI = 3.14
    # Bad:  pi = 3.14


# NOTE: In bigger programs, the variable name should describe what its value represents
# This again makes the code more readable for yourself and for others