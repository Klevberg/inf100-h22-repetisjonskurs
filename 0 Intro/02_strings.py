print("Strenger skrives mellom hermetegn.")
print('Man kan også bruke apostrof.')
# print(Hvis du ikke har hermetegn er det ikke en streng, og programmet krasjer)


# En streng kan lagres i en variabel.
tekst = "hei"

print("tekst") # Skriver ut "tekst"
print(tekst) # Skriver ut "hei"


# En streng kan inneholde linjeskift (\n)
print("Denne strengen\ninneholder to\nlinjeskift")


# En streng kan inneholde hermetegn (")
print("Her \"er\" et hermetegn")
print('Her "er" et hermetegn') # bedre: bruk apostrofer


# len() funksjonen finner lengden til en streng
print(len("Hei!")) # 4
print(len("kul streng")) # 10

x = "INF100"
print(len(x)) # 6


# En streng kan være tom
x = ""
print(len(x)) # 0
print(x) # printer ingenting på denne linjen


# Strenger slås sammen med pluss (+)
print("fiske" + "boller") # fiskeboller

a = "Veldig"
b = "kult"
print(a + " " + b) # Veldig kult


# Strenger repeteres flere ganger med gangesymbol (*)
print("A" * 5) # AAAAA

s = "ha"
print(3 * s) # hahaha


# LIFE HACK: f-strenger

# Med en f-streng kan vi inkludere variabler i strengen
number_of_students = 800
course_id = "INF100"
print(f"Vi ønsker {number_of_students} studenter velkommen til {course_id}")

# Uten f'en får vi en logisk feil
print("Vi ønsker {number_of_students} studenter velkommen til {course_id}")
print()

# f-strenger kan også brukes for å lage verdier som lagres som en variabel
message = "Jeg lengter hjem"
log_message = f"Mottatt melding: {message}"
print(log_message) # "Mottatt melding: Jeg lengter hjem"

# f-strenger er ikke magiske
message = "Jeg er fornøyd"
print(log_message) # fremdeles "Mottatt melding: Jeg lengter hjem"
