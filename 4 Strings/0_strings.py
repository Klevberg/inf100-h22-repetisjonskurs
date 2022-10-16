# We can use either double or single quotes to represent strings
print('foo' == "foo")  # True


# This is how we use quotes in our strings
print("Let's use 'single quotes'")
print('Let\'s use "double quotes"')
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


newline = "New\nline"

print(str(newline))
print(repr(newline))


print("abc" + "def")    # concatenation
print("abc" * 3)        # repetition


# Membership
print("a" in "abc")
print("bc" in "abc")
print("ca" in "abc")
