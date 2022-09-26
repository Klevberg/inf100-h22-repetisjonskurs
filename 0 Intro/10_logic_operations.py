# We look at not, and, or


# 'not' returns the opposite of a boolean value
print(not True) # False
print(not False) # True
print(not "") # True
print(not -2) # False


print()


# The 'and' operator returns truthy if both sides are true and it returns falsy if not
# In particular, 'and' returns...
    # 1. False if either side is falsy and the left part is True
    # 2. the left value if it is falsy
    # 3. the right value if both sides are truthy
print(False and False)  # False
print(False and True)   # False
print(True and False)   # False
print(True and True)    # True
print(True and 5)       # 5
print(0 and "hi")      # 0
print(2 and 3)          # 3
print(False and None)   # False


print()


# The 'or' operator returns truthy at least one of the sides are truthy
# In detail, the 'or' operator returns...
    # 1. True if either side is truthy and the right part is False
    # 2. the left part if the left part is truthy
    # 3. the right part otherwise
print(False or False)   # False
print(False or True)    # True
print(True or False)    # True
print(True or True)     # True
print(True or 5)        # True
print(0 or "hello")     # "hello"
print(2 or 3)           # 3
print(False or None)    # False
