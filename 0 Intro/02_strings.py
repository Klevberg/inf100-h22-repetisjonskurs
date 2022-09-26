print("Strings are written between quotation marks")
print('We can either use double or single quote marks.')
# print(If you do not use quotation marks then it is not a string, and the program will crash)


# A string can be stored in a variable
text = "hello"

print("text") # Prints the word "text"
print(text) # Prints the word "hello"


# A string can contain newlines (\n)
print("This string\ncontains two\nnewlines")


# A string can contain quotation marks (")
print("\"goodbye\", she said")   # We cancel them using \ to tell Python that we do not wish them to affect the full string
print('"why", he said')          # Or better: we can use single quotes


# The len() function finds the length of a string
print(len("Hi!")) # 3
print(len("cool string")) # 11

x = " INF100   "
print(len(x)) # 10


# A string can be empty
x = ""
print(len(x)) # 0
print(x) # prints nothing (only a new line)


# Strings can be put together with the plus sign (+)
print("fiske" + "boller") # fiskeboller

a = "Very"
b = "cool"
print(a + " " + b) # Very cool


# Strings can be repeated multiple times using the multiplication sign (*)
print("A" * 5) # AAAAA

s = "ha"
print(3 * s) # hahaha


# LIFE HACK: f-strings

# Using an f-string we can insert variables directly into the string
number_of_students = 683
course_id = "INF100"
print(f"There are {number_of_students} students taking the {course_id} course")
print()

# Without the f, the brackets as well as the variable names will be printed instead
print("There are {number_of_students} students taking the {course_id} course")
print()
