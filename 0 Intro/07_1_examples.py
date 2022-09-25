
print("Operatøren / utfører 'vanlig' divisjon")
print(" 7/4  =", ( 7/4))  # 1.75
print()
print("Operatøren // utfører heltallsdivisjon:")
print(" 7//4 =", ( 7//4)) # 1 (runder nedover)
print(" 5//4 =", ( 5//4))
print("-1//4 =", (-1//4)) # -1 (runder også nedover)
print("-7//4 =", (-5//4))
print("Når nevneren er negativ")
print(" 7//-4 =", (7//-4)) # -2 (runder også nedover)
print("-7//-4 =", (-7//-4)) # 1 (runder alltid nedover)


# The types determine what the operation does
print(3 * 2)
print(3 * "abc")
print(3 + 2)
print("abc" + "def")
# print(3 + "def") # Crash!

import math
# The math.ceil() function always rounds up
print("math.ceil(3.1) =", math.ceil(3.1)) # 4
print("math.ceil(-3.9) =", math.ceil(-3.9)) # -3
# The math.floor() function always rounds down
print("math.floor(3.9) =", math.floor(3.9)) # 3
print("math.floor(-3.1) =", math.floor(-3.1)) # -4