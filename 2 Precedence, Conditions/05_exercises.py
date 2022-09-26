# Fix the mistakes

def valid_choice(input):
    if input == ("Rock" or "Paper" or "Scissors"):
        return True
    else:
        return False

print(valid_choice("Paper"))


# What does the following line of code print, and in what order?

print(print("Rock") or print("Paper") and print("Scissors"))
