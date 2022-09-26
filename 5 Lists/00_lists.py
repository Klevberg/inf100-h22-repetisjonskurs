"""
Show examples of lists
Can store multiple types of elements, and other lists
Loop through a list
Examples etc.

Same with tuples
"""


def eks_1():
    lst = [1, "Hello", " ", 3, "World!", [3, 2, 1]]
    print(lst)
    print(lst[1] + lst[2] + lst[4])


def eks_2():
    # IKKE MUTER EN LISTE INNI EN FOR-HVER -LØKKE!
    # Vil ikke krasje, men gjør heller ikke som vi forventer
    a = [3, 3, 2, 3, 4]
    print("a =", a)

    # Mislykket forsøk på å fjerne alle 3'erne
    for item in a:
        if item == 3:
            a.remove(item)

    print("a =", a)


def eks_3():
    # Bedre: mutering i en while-løkke.
    # Her har vi full kontroll på hvordan indeks endrer seg.
    a = [3, 3, 2, 3, 4]
    print("a =", a)

    # Vellykket forsøk på å fjerne alle 3'erne
    index = 0
    while index < len(a):
        if a[index] == 3:
            a.pop(index)
        else:
            index += 1

    print("Huzza! a =", a)


def eks_4():
    # Sortering
    a = [7, 2, 5, 3, 5, 11, 7]
    print("Først, a =", a)
    a.sort()
    print("Etter a.sort(), a =", a)
    print("---")

    # Reversering
    a = [2, 3, 5, 7]
    print("Først, a =", a)
    a.reverse()
    print("Etter a.reverse(), a =", a)


def eks_5():
    # Sortering
    a = [7, 2, 5, 3, 5, 11, 7]
    print("Først, a =", a)
    b = sorted(a)
    print("Etter b = sorted(a)")
    print("    a =", a)
    print("    b =", b)
    print("---")

    # Reversering
    a = [2, 3, 5, 7]
    print("Først, a =", a)
    b = reversed(a)
    c = list(reversed(a))
    print("Etter b = reversed(a)  og  c = list(reversed(a))")
    print("    a =", a)
    print("    b =", b)
    print("    c =", c)
    print("Her er elementene i b:")
    for x in b:
        print(x, end=" ")
    print()

    print("Her er elementene i b en gang til (men hæ???):")
    for x in b:
        print(x, end=" ")
    print()
    print("---")


def eks_6():
    a = ["Florida", 15.4, "2022-09-16"]

    place, temp, date = a
    print(f"{place = }", f" {temp = }", f" {date = }", sep="\n")


def eks_6():
    a = ["Florida", 15.4, "2022-09-16"]

    place, temp, date = a
    print(f"{place = }", f" {temp = }", f" {date = }", sep="\n")


def eks_7():
    a = ["Florida", 15.2, 13.5, 17.2, 13.6, 14.2]

    place, *temps = a
    print(f"{a=}")
    print(f"{place=}")
    print(f"{temps=}")


def eks_8():
    a = ["Florida", "not interested", 15.2, 13.5, 17.2, 13.6, 14.2, "OK"]

    place, _, *temps, last_temp, status = a

    print(f"{a         = }")
    print(f"{place     = }")
    print(f"{_         = }")
    print(f"{temps     = }")
    print(f"{last_temp = }")
    print(f"{status    = }")


def eks_9():
    a = [1, 2]
    b = [3, 4]
    c1 = [a, b]  # En liste av lister -- en 2-dimensjonell liste
    c2 = [*a, *b]  # En liste med verdiene fra to lister -- en "flat" liste
    c3 = a + b
    c4 = b + a
    print(a, b, c1, c2, c3, c4, sep="\n")


def eks_10():
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    print(c)
    print("c[0][0] =", c[0][0])
    d = (1, 2)


def eks_11():
    # Den lange måten
    a = []
    for i in range(10):
        a.append(i + 1)
    print(a)


def eks_12():
    # Med listeforståelse
    a = [i + 1 for i in range(10)]
    b = list(range(1, 10))
    print("a =", a)
    print("b =", b)


def eks_13():
    # For de ambisiøse: listeforståelse med betingelser
    a = [i + 1 for i in range(20) if i % 2 == 0]
    print(a)

    # Listeforståelse for å ikke-destruktivt filtrere en liste
    def divisible_by_3(x):
        return x % 3 == 0

    b = [x for x in a if divisible_by_3(x)]
    print(b)

    # Listeforståelse for å ikke-destruktivt anvende en funksjon på
    # hvert element i en liste
    def square(x):
        return x * x

    c = [square(x) for x in b]
    print(c)

    d = ["d" for _ in range(10)]
    print(d)

    e = [[i for i in range(3)] for _ in range(3)]
    print(e)


def eks_14():
    print("Summen av alle tall under 1000 som er delelig med 3 eller 5")
    print(sum([i for i in range(1001) if i % 3 == 0 or i % 5 == 0]))


def eks_15():
    lst = [1, 2, 3, 4, 5]
    print("lst[start:end:step]")
    print("lst[-1] =", lst[-1])
    print("lst[1:2] =", lst[1:2])
    print("lst[1:] =", lst[1:])
    print("lst[:1] =", lst[:1])
    print("lst[::2] =", lst[::2])
    print("lst[-1:0:-1] =", lst[-1::-1])
