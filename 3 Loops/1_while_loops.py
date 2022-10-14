# We use while loops when we want some code to loop as long as some condition holds true

def example_1():
    # Print as long as x is less than 5
    x = 0
    while x < 5:
        print("x:", x)
        x += 1

# example_1()


def example_2():
    # A better example of a while loop

    total = 0
    number = 0

    # This while loop will keep looping until the input is 'quit'
    while number != 'quit':
        total += int(number)
        print('The total is', total)
        number = input('Give me a new number to add: ')

# example_2()