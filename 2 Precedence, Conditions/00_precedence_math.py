# The rules of precedence decide which operations solve before others

# In math, division has higher precedence than addition
print( 4 + 6 / 2 )

print( (3 + 6) * 2 - 9 / 3 + 5 )

# ** has higher precedence than *
print(2**3*4) # 32, not 4096

# Association
print(9-8-4)   # -3, not 5 (- assosiates from left to right)
print(4**3**2) # 262144, not 4096 (** assosiates from right to left)