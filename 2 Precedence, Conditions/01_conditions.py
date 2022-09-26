# Datatype bool: True / False

name = "August"
age = 24
is_nervous = True


# Simple condition: if

if is_nervous:
    print(f"{name} is nervous")


print()


# Operators for relation / comparison: ==, !=, <, >, <=, >=

print(age == 20)
print(age >= 18)

if age >= 18:
    print(f"{name} is an adult")


print()


# if / else

if age >= 18:
    print(f"{name} is an adult")
else:
    print(f"{name} is not an adult")


print()


# if / elif / else


my_bool = True

if my_bool:
    print("my_bool was true")
elif not my_bool:
    print("my_bool was false")
else:
    print("Will never happen")


print()


my_num = 101

if my_num > 100:
    print("This number was bigger than 100")
elif my_num < 100:
    print("This number was smaller than 100")
else:
    print("This number was equal to 100")


print()


amount_of_cats = 1

if amount_of_cats == 0:
    print(f"{name} has no cats")
elif amount_of_cats == 1:
    print(f"{name} has one cat")
elif amount_of_cats > 1:
    print(f"{name} has multiple cats")
else:
    print("Cannot have negative cats")


# What's the difference between using a chain of if / elif / else vs using multiple if statements?

# From the second lab:

def find_longest_words(word_1, word_2, word_3):

    longest_length = max(len(word_1), len(word_2), len(word_3))

    if len(word_1) == longest_length:
        print(word_1)
    if len(word_2) == longest_length:
        print(word_2)
    if len(word_3) == longest_length:
        print(word_3)

find_longest_words("Game", "Action", "Champion")
find_longest_words("apple", "carrot", "ananas")
find_longest_words("Four", "Five", "Nine")
print()


def find_first_longest_word(word_1, word_2, word_3):

    longest_length = max(len(word_1), len(word_2), len(word_3))

    if len(word_1) == longest_length:
        print(word_1)
    elif len(word_2) == longest_length:
        print(word_2)
    else:
        print(word_3)

find_first_longest_word("Game", "Action", "Champion")
find_first_longest_word("apple", "carrot", "ananas")
find_first_longest_word("Four", "Five", "Nine")
