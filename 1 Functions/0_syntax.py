# We define a function like this:
def function_name():
    # First line of code to be executed here
    # Second line of code here
    # Third line (note the indentation)
    some_value = 2
    print("Hello from inside the function")
    
    return some_value # Optional return at the end

print("Hello from outside the function")

# The function will never be executed unless we tell Python to run it
# We "call" a function like this:
function_name()
print("Hello from outside the function")


# NOTE: The function name should describe its job


# This function will print a nice picture of an owl

def owl_surprise():
    print(' ,  ,\n {o,o} <(coucou)\n./)_)\n  " "')

owl_surprise()

# We can call this function as many times as we want
# owl_surprise()
# owl_surprise()
# owl_surprise()
