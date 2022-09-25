# When we return a value from the function, we tell it to "give back" this value to where we called the function
def plus_two(n):
    return n + 2

number = 3

print(plus_two(number))

# The variable number is unchanged (still 3)
number = plus_two(number)
# number is 5
number = plus_two(number)
# number is 7
print(number)

# NOTE: return is a statement, not a function
# We do not write it as return(some_value), but as: return some_value


"""
One of the main issues that we've seen our students meet is understanding when
to use return, print, or nothing within a function.

When we call a function, we jump to another place in code. After the function
is finished running, we will jump back to where we called the function. Using
function parameters, we can send information into a function. But how can we 
send information back? That's where the return statement comes in.

If we use a return statement in a function, we can send information back from
the function.

If we only want the function to print some text to the terminal (program output),
we can use the print() function once or several times.

If we want the function to do neither, then we use neither return nor print.
"""

# The differences between return and print()

# return
    # is a statement
    # sends information back to where we called the function
    # stops the function

# print()
    # is a function
    # prints some text to the terminal
    # does not stop the function