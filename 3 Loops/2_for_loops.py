# We use a for loop when we know exactly how many times we want to loop

# Prints each letter of the string "Hello", one at a time
def example_1():
    string = "Hello"
    # Since the string "Hello" has five letters, we know that we want to loop five times

    print("Before")

    for letter in string:
        print(letter)
    
    print("After")

# example_1()


# Prints "Hello" five times
def example_2():
    for _ in range(5):
        print("Hello")

# example_2()


# Let's take a closer look at range()

test_range = range(5)
# print(test_range)

test_range = list(test_range)
# print(test_range)

# range(start, end, step)
# range(start, end)
# range(end)                # starts from 0


def example_3():
    for i in range(5):
        print("This is loop number", i)

# example_3()


# What is an index?

# Think of index as another word for position

# In programming we usually start counting from zero

# Using an index, we can grab a certain letter from a string, or an item from a list

# Say we want to grab the second letter of string "avocado"
# We use square brackets after the string or variable name, and specify the index

string = "avocado"
# print(string[1]) # Since we start counting from zero, position two would be index one


# What if we want to loop through "hello" and count while doing so?
# We can use 'i' as an index

string = "hello"

test_range = range(len(string))
# print(list(test_range))


def example_4():
    string = "hello"

    for i in range(len(string)):
        print(i, string[i])

# example_4()