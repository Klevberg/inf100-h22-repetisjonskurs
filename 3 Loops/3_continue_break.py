# continue skips ahead to the next iteration of a loop

def example_1(n):
    for i in range(n):
        if i % 3 == 0:
            continue

        print(i)

# example_1(20)


# break exits a loop

def example_2():

    count = 0

    while True:
        print("Loop", count)
        response = input("Do you wish to continue? (yes/no): ")
        if response.lower() == "yes":
            count += 1
        elif response.lower() == "no":
            break
    
    print("Goodbye")

# example_2()


def example_3(string):

    for i in range(len(string)):
        if string[i] == 'a':
            print("The index of character 'a' is", i)
            break
    else:
        print(f"The character 'a' does not exist in the string '{string}'")

# example_3("elephant")