weather = ["Florida", 15.4, "2022-09-16"]

place, temp, date = weather
print(f"At {date}, {place} saw a temperature of {temp} degrees.")
print()


weather = ["Florida", 15.2, 13.5, 17.2, 13.6, 14.2, 16.1, 15.5]

place, *temps = weather
print(place)
print(temps)
print()


weather = ["Florida", "code_6528", 15.2, 13.5, 17.2, 13.6, 14.2, "OK"]

place, _, *temps, status = weather

print(place)
print(temps)
print(status)
