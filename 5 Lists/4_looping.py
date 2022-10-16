fruits = ["apple", "pineapple", "pear", "apple", "mango", "banana"]


# Loop through each element in a list
for fruit in fruits:
    print(fruit)
print()


# Loop through a list using indexing
for i in range(len(fruits)):
    print(i, fruits[i])
print()


# Using enumerate()
for i, fruit in enumerate(fruits):
    print(i, fruit)
print()


# Remove all apples from list using a while loop
while "apple" in fruits:
    fruits.remove("apple")

print(fruits)
