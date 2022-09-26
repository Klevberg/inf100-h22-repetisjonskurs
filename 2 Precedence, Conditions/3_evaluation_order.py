# The evaluation order (evalueringsrekkefølge) determines in what order expressions are evaluated

def one():
    print("one", end=" ")
    return 1

def two():
    print("two", end=" ")
    return 2

def three():
    print("three", end=" ")
    return 3

print(one() + two() * three()) # one two three 7


print()


# Short-circuit evaluation (kortslutningsevaluering)
def yes():
    return True

def no():
    return False

def crash():
    return 1/0

print(no() and crash()) # False (Python never runs the crash() function)
#print(crash() and no()) # Crashes!

print(yes() or crash()) # True (Python never runs the crash() function)
#print(crash() or yes()) # Crashes!
