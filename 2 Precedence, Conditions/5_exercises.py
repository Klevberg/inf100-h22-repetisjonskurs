# Fix the mistakes

def valid_choice(input):
    if input == ("Rock" or "Paper" or "Scissors"):
        return True
    else:
        return False

print(valid_choice("Paper"))


print()


# What does the following line of code print, and in what order?

def print_one():
    print(1)
    return 0

print(print("3") or print_one() and print("2"))
