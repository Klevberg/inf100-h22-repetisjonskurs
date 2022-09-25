# The operator / executes a regular division
print("7/4 =", 7/4)  # 1.75
print()

# The operator // executes a whole number division
print("7//4 =", ( 7//4)) # 1 (rounds down)
print("-1//4 =", (-1//4)) # -1 (also rounds down)


# The types determine what the operation does
print(3 * 2)        # 6
print(3 * "abc")    # "abcabcabc"
print(3 + 2)        # 5
print("ab" + "cd")  # "abcd"
# print(3 + "def")  # Crash!


import math

# The math.ceil() function always rounds up
print("math.ceil(3.1) =", math.ceil(3.1)) # 4
print("math.ceil(-3.9) =", math.ceil(-3.9)) # -3

# The math.floor() function always rounds down
print("math.floor(3.9) =", math.floor(3.9)) # 3
print("math.floor(-3.1) =", math.floor(-3.1)) # -4