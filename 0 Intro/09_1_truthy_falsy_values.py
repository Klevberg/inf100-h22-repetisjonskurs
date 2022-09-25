# Any value can be interpreted as a boolean value

print("yes" if True else "no") # yes

print("yes" if 1 else "no") # yes

print("yes" if "Hello" else "no") # yes

print("yes" if "0" else "no") # yes

print("yes" if 0 else "no") # no

print("yes" if "" else "no") # no

print("yes" if None else "no") # no
