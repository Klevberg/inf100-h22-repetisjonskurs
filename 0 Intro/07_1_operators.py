# The operator / executes a regular division
print(7 / 4)  # 1.75

print()

# The operator // executes a whole number division
print(7 // 4) # 1 (rounds down)
print(-1 // 4) # -1 (also rounds down)


print()


# The operator % (modulo) gives us the remainder after dividing
print(6 % 3) # 0
print(5 % 2) # 1
print(5 % 3) # 2
print(0 % 3) # 0


print()


# The operator ** is used for exponentiation
print(2**2) # 4
print(3**3) # 27
print(4**3) # 64


print()


# The types determine what the operation does
print(3 * 2)        # 6
print(3 * "abc")    # "abcabcabc"
print(3 + 2)        # 5
print("ab" + "cd")  # "abcd"
# print(3 + "def")  # Crash!


print()


import math

# The math.ceil() function always rounds up
print("math.ceil(3.1) =", math.ceil(3.1)) # 4
print("math.ceil(-3.9) =", math.ceil(-3.9)) # -3

# The math.floor() function always rounds down
print("math.floor(3.9) =", math.floor(3.9)) # 3
print("math.floor(-3.1) =", math.floor(-3.1)) # -4
