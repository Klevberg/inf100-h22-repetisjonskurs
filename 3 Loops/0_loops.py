"""
Show a few examples of while-Loops.
Mix in with questions like, how many iterations will the loop iterate, output, etc.

Show a few examples of for-Loops
mix in questions, show a for-loop as a while-loop.
"""


def eks_1():
    x = 0
    while x < 5:
        print("x: ", x)
        x += 1


def eks_2():
    name = ''
    # Will iterate till the input is "your name"
    while name != 'your name':
        name = input('Please type your name: ')


def eks_3():
    even = []
    odd = []
    numbers = [1, 1, 1, 3, 4, 5, 6, 7, 8, 34, 56, 6, 1, 3, 9, 4]
    # Will sort the list into even or odd numbers
    while len(numbers) > 0:
        # Removes the element in the list in the index 0
        num = numbers.pop(0)
        # Checks if even or odd, and adds in the corresponding list
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    print("Even numbers: ", even)
    print("Odd numbers: ", odd)


def eks_4():
    a = 1
    b = 10
    # Loops while a is less than b + 1
    while a < b + 1:
        print(a)
        a + 1  # Is not assigned to a, so will loop forever


def eks_5():
    lst = [1, 3, 5, 10, 5]
    # Finds the index where a is stored
    a = 5
    i = 0
    while i < len(lst):
        print("i: ", i)
        if a == lst[i]:
            print("a: " + str(a) + " is on index: " + str(i))
        i += 1
        
        
def eks_6():
    lst = [1, 3, 5, 10, 5]
    # Finds the index where a is stored
    a = 5
    i = 0
    while i < len(lst):
        print("i: ", i)
        if a == lst[i]:
            print("a: " + str(a) + " is on index: " + str(i))
            break
        i += 1
        

def eks_7():
    even = []
    numbers = [1, 1, 1, 3, 4, 5, 6, 7, 8, 34, 56, 6, 1, 3, 9, 4]
    # Will sort the list into even numbers
    while len(numbers) != 0:
        # Removes the element in the list in the index 0
        num = numbers.pop(0)
        # Checks if even, and adds it to the list
        if num % 2 != 0:
            continue
        even.append(num)

    print(even)


def eks_8():
    print("For-loop")
    for i in range(10):
        print(i)
    j = 0
    print("While-loop")
    while j < 10:
        print(j)
        j += 1


def eks_9():
    for i in range(3):
        for j in range(3):
            print(i, j)


def eks_10():
    for i in range(3):
        for j in range(3):
            if i == 1 or j == 1:
                continue
            print(i, j)
            
            
def eks_11():
    for i in range(3):
        for j in range(3):
            if i == 1 or j == 1:
                break
            print(i, j)
