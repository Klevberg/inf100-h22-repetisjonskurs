def eks_1():
    # I kildekoden kan streng-verdier oppgis på fire ulike måter
    print('apostrof')
    print("hermetegn")
    print('''trippel-apostrof''')
    print("""trippel-hermetegn""")

    # Hvilken variant som brukes har absolutt ingenting å si
    print('foo' == "foo")  # True

    # Så hvorfor ha flere varianter?
    # Svar 1: kompabilititet
    # Svar 2: for å enklere skrive hermetegn og apostrof
    print("Her er 'apostrof'")
    print('Her er "hermetegn"')
    print("""Her er både "hermetegn" og 'apostrofer'""")


def eks_2():
    print("Hermetegn i hermetegn-streng: \"")
    print("Bakstrek: \\")
    print("Linjeskift: [\n]")
    print("Tab: [\t]")
    print()

    print("Denne teksten er skilt av tab'er, 3 per linje:")
    print("abc\tdef\tg\nhi\tj\\\tk\n---")
    print()

    # En escape-sekvens telles som ett tegn
    s = "a\\b\"c\td"
    print("s =", s)
    print("len(s) =", len(s))


def eks_3():
    def print_string_conversion(x):
        print("type:", type(x))
        print(" str:", str(x))
        print("repr:", repr(x))
        print()

    print("Vanligvis konverteres verdier til streng med str-funksjonen")
    print("Å bruke repr-funksjonen gir for mange vanlige typer samme resultat")
    print_string_conversion(10)
    print_string_conversion(True)
    print_string_conversion(2 / 11)

    print("Men for strenger, viser repr oss whitespace og escape-sekvenser.")
    print_string_conversion("   Mellomrom\ttab   ")
    print_string_conversion("Linje\nskift")

    # Generelt vil `repr` vise mer detaljert informasjon enn `str`.
    # Hensikten med `str` er at resultatet skal være leselig, hensikten
    # med `repr` er å gi oss presis informasjon.

    print("For andre typer kan forskjellen være stor")
    import datetime
    today = datetime.datetime.now()
    print_string_conversion(today)


def eks_4():
    s = "abcdef"
    print(s[0])
    print(s[-1])
    print(s[1:4:2])


def eks_5():
    print("abc" + "def")  # Konkatenasjon
    print("abc" * 3)  # Repetisjon
    print(len("abc"))  # Lengde
    print()

    # Medlemskap
    print('"a" in "abc"')
    print("a" in "abc")
    print('"bc" in "abc"')
    print("bc" in "abc")
    print('"ca" in "abc"')
    print("ca" in "abc")
    print('"A" in "abc"')
    print("A" in "abc")
    print('"" in "abc"')
    print("" in "abc")
    

def eks_6():
    a = "abcdef"
    print(a)
    print(a.capitalize())
    print(a.upper())
    
    print(f"is a upper")


def eks_7():
    a = "abcdef"
    print(a)
    print("for i in range(len(a))")
    for i in range(len(a)):
        print(a[i])
    print("for c in a")
    for c in a:
        print(c)


def eks_8():
    a = "abcdef"
    print(a)
    for i in range(len(a)):
        a[i] = "a"
    print(a)
