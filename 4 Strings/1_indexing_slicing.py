s = "Hello, world"

# Indexing of strings

print(s[0])     # H
print(s[3])     # l
print(s[-1])    # d
print(s[-3])    # r
print()


# Slicing of strings

# s[start:end]
# s[start:end:step]

print(s[2:4])   # ll
print(s[1:4:2]) # el
print(s[:3])    # Hel
print(s[2:])    # llo, world
print(s[::2])   # Hlo ol
print()


# Reverse order of string

print(s[::-1])  # dlrow ,olleH
print()


# What will the following print?

s = "Hello, world"
# print(s[2::3])
