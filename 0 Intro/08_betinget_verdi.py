# A conditional value allows us to choose the value depending on a condition
print("yes" if True else "no")  # yes
print("yes" if False else "no") # no

# We can read it as follows:
# Give me "yes" if one is less than or equal to two. Otherwise, give me "no"
print("yes" if 1 <= 2 else "no") # yes


print()


x = -5

# Using this we can for example print whether a number is positive or negative
print("negative" if x < 0 else "positive")

# or we can print whether a number is odd or even
print("even" if x % 2 == 0 else "odd")
