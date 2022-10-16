# Unlike strings, lists are mutable, which means we can change them directly

numbers = [8, 5, 2, 7]


# Set the first element to 1 (indeks 0)

numbers[0] = 1
print(numbers)


# The .append() method adds an element to the end of a list

numbers.append(4)
print(numbers)

# The following is incorrect usage of .append(). Since it does not return anything,
# None will be assigned to the numbers variable

# numbers = numbers.append(4)
# print(numbers)


# The .insert() method can add an element to anywhere in the list.
# This is specified using an index

# numbers.insert(index, element)

numbers.insert(2, 5)    # The number 5 is added in the third slot (indeks 2)
print(numbers)          # The remaining elements in the list are pushed over by one slot


# The .extend() method extends one list with another

more_numbers = [3, 4]
numbers.extend(more_numbers)
print(numbers)

# If we try adding more numbers with append, we will add the entire list, and
# not each elements within

# tall.append(more_numbers)
# print(numbers)


# The .remove() method removes the first case of a specified element from a list

print(numbers)

numbers.remove(5)
print(numbers)

# Again, we remove the first case of the number 5 from the list

numbers.remove(5)
print(numbers)

# If we try doing so once more, we will get an error, since the number 5 no
# longer exists in the list

# numbers.remove(5)
# print(numbers)


# The .pop() method removes an element from the list positioned at a specified index

numbers.pop(0)
print(numbers)

# An empty .pop() will always remove the last element of a list

numbers.pop()
print(numbers)


# The .sort() method sorts a list from lowest to highest in value

# numbers.sort()

# We can also specify reverse=True as an argument to get it sorted from highest
# to lowest in value

# numbers.sort(reverse=True)
# print(numbers)

# .sort() vs sorted()

# sorted() is a built-in function, not a method. It returns a new list,
# like the previous, now sorted

# numbers = sorted(numbers)
# print(numbers)


# The .reverse() method will reverse the order of a list

numbers.reverse()
print(numbers)

# The .clear() method empties a list

# numbers.clear()
# print(numbers)


# The .count() method counts and returns the number of a certain element in a list

print(numbers.count(4)) # We count the number of number 4 in the list


# The .index() method finds and returns the index of the first case of an certain
# element in a list

print(numbers.index(4))
