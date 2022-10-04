# We can use either double or single quotes to represent strings
print('foo' == "foo")  # True
print()

# This is how we use quotes in our strings
print("Let's use 'single quotes'")
print('Let\'s use "double quotes"')
print()

print("abc" + "def")    # concatenation
print("abc" * 3)        # repetition
print(len("abc"))       # length
print()

# The backslash can be used to 'escape' a character
print("Newline: [\n]")  # becomes a newline
print("Tab: [\t]")      # becomes a tab
print("Backslash: \\")  # becomes a backslash
print()

# An escaped character counts as a single character
string = "a\\b\"c\td"
print("string =", string)
print("len(string) =", len(string))


def print_string_conversion(x):
    print("type:", type(x)) # shows the type of a variable x
    print(" str:", str(x))  # shows the string as represented in the terminal
    print("repr:", repr(x)) # shows the string as stored in the variable x
    print()

print_string_conversion(10)
print_string_conversion(True)
print_string_conversion(2 / 11)

print_string_conversion("Mellomrom\ttab")
print_string_conversion("Linje\nskift  ")


s = "abcdef"

# Indexing of strings
print(s[0])
print(s[-1])

# Slicing of strings
print(s[1:4:2])


# Membership
print("a" in "abc")
print("bc" in "abc")
print("ca" in "abc")


# Loop through each character in a string
for c in s:
    print(c)


# Loop through a string using indexing
for i in range(len(s)):
    print(i, s[i])
    # s[i] = "x" # Crash
print()


# String methods: https://www.w3schools.com/python/python_strings_methods.asp
print(s)
print()

print(s.capitalize())
print(s)
print()

s = s.upper()
print(s)
print()

s = s.lower()
print(s)
print()

print(s.count('b'))
print(s.index('c'))
print()

s = ' hello    \n'
print(s)
print(len(s))
print()

s = s.strip()
print(s)
print(len(s))
