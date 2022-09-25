# Scope is important to understand to know where variables exist within a program

def just_print(x):
    print(x)

just_print(2) # prints 2
#print(x) # crashes! The variable x only exists within the scope of the function


print()


def print_42():
    y = 42
    print(y)

print_42() # prints 42
#print(y) # crashes for the same reason as above


print()


# A good exercise is to comment the values along the way
def add_four(x):
    x += 4
    return x

def find_xyz(x):
    y = add_four(x*2)
    z = add_four(y)
    return x + y + z

print(find_xyz(2))


print()


x = "x in the global scope"
y = "y in the global scope"

def function():
    y = "y in local scope"
    z = "z in local scope"
    print(x)
    print(y)
    print(z)

function()


"""
The parameter of a function and the variable that gets sent into
the function do not have to share name as they have no effect on
eachother
"""
