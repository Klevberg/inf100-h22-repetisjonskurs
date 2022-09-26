# We look at not, and, or


# 'not' returns the opposite of a boolean value
print(not True)     # False
print(not False)    # True
print(not "")       # True
print(not -2)       # False


print()


# The 'and' operator returns truthy if both sides are true and it returns falsy if not
# In particular, 'and' returns the left part if the left part is falsy, otherwise it will return the right part
print(False and False)  # False
print(False and True)   # False
print(True and False)   # False
print(True and True)    # True
print(True and 5)       # 5
print(0 and "hi")       # 0
print(2 and 3)          # 3
print(False and None)   # False


print()


# The 'or' operator returns truthy at least one of the sides are truthy
# In detail, 'or' returns the left side if the left side is truthy, otherwise it will return the right side
print(False or False)   # False
print(False or True)    # True
print(True or False)    # True
print(True or True)     # True
print(True or 5)        # True
print(0 or "hello")     # "hello"
print(2 or 3)           # 2
print(False or None)    # None
