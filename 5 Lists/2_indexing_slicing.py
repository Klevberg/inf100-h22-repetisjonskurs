fruits = ["apple", "pineapple", "pear", "mango", "banana"]


# Indexing
print(fruits[3])    # "mango"

my_list = [1, "Hello", ", ", 3, "world!", [3, 2, 1]]
print(my_list[1] + my_list[2] + my_list[4]) # Hello, world!

print(my_list[-1])  # [3, 2, 1]
print()


# Slicing

# fruits[start:end]
# fruits[start:end:step]

print(fruits[1:3])  # ['pineapple', 'pear']
print(fruits[2:])   # ['pear', 'mango', 'banana']
print(fruits[:4])   # ['apple', 'pineapple', 'pear', 'mango']
print(fruits[:4:2]) # ['apple', 'pear']
print(fruits[::-1]) # ['banana', 'mango', 'pear', 'pineapple', 'apple']
