# The input() funksjon lets us get input from the user through the terminal
name = input("Enter your name: ")
print(f"Hello, {name}!")


# What if we use input() without assigning it to a variable?
input("Press enter to continue... ")


string = input("Enter the string you want me to repeat: ")
# If we write "cou", Python will print "coucou"
print(string * 2)


# Be careful! Input will always give us a value of type string
number = input("Give me a positive number: ")
number = number * 2
# If we entered the number 5, Python will print "55" instead of 10
print(number)


# This code will make the program crash!
number = input("Give me a positive number: ")
number = number + 2
print(number)

# We cannot (put together) / (get the sum of) a string and a number
