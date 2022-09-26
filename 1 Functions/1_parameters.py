# A parameter allows us to communicate with the function by sending it a value
def print_n_plus_two(n):
    print(n + 2)

number = 3

print_n_plus_two(number)


# NOTE: When a problem tells us that the parameter is of a certain type, we can assume that it is so

''' We won't have to do something like this:
def times(a, b):
    int(a)
    int(b)
'''


# Parameters let us interact with the function code from outside of the function
def owl_surprise(owl_speech):
    print(' ,  ,\n {o,o} <(' + owl_speech + ')\n./)_)\n  " "')

string = "Hello"
owl_surprise(string)


# This function will take a number and double it
def double(number):
    return number*2

n = 2
n = double(n)
print(n)


# This function will take a width, length, and height of a box and find the volume
def volume_of_box(width, length, height):
    return width, length, height

width = 3
length = 2
height = 5

volume = volume_of_box(width, length, height)