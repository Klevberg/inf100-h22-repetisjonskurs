# List comprehensions - Build lists using less space

numbers = [4, -3, 1, 9 -1, 0, -6, 5]


# This function does the same as the double_non_destructive() function
def double(numbers):
    return [x*2 for x in numbers]

print(double(numbers))


def get_positive_numbers(numbers):
    return [x for x in numbers if x > 0]

print(get_positive_numbers(numbers))


def change_negatives_to_none(numbers):
    return [x if x >= 0 else None for x in numbers]

print(change_negatives_to_none(numbers))


# Some more examples

def divisible_by_3(x):
    return x % 3 == 0

print( [x for x in numbers if divisible_by_3(x)] )


def square(x):
    return x * x

print( [square(x) for x in numbers] )


print( [0 for _ in range(10)] )


# The sum of all numbers up to 1000 that are divisible by 3 or 5
print( sum([x for x in range(1000 + 1) if x % 3 == 0 or x % 5 == 0]) )
