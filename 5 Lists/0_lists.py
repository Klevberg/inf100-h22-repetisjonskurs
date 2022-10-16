# Making a list
fruits = ["apple", "pineapple", "pear", "mango", "banana"]
print(fruits)

# The order is important, it will not change unless we change it directly


# Find the length of a list
print(len(fruits))


# Lists can hold different data types
liste = [1, 2, 3, 4, 5, 6]
liste2 = [True, False, False]
liste3 = ['hello', 1, True, 1.9] # This list holds several different data types


# Membership: We can check whether the string 'mango' exists in the list of fruits
if 'mango' in fruits:
    print('Yes')
else:
    print('No')
