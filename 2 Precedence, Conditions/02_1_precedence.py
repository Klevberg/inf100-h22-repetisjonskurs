print(True or True and False)   # True
print(not False or True)        # True
print(not (False or True))      # False

print()

print(2 < 3 < 4)            # True
print(not 3 < 2 < 1)        # True
print(not 3 < 2 and 1 < 2)  # True

print()

print("e" in "hello")           # True
print("e" in "hello" == True)   # False
print("a" and "e" in "hello")   # True
print("x" or "y" in "hello")    # "x"
