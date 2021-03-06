# Temainnlevering 5
# Sondre Knutsen (skn003)


# Oppgave 1
def siste(sekvens):
    return sekvens[-1]


print("siste('Python'):", siste('Python'), '\n')


# Oppgave 2
def skrivsekvens(sekvens):
    for c in sekvens:
        print(c, end=" ")


skrivsekvens([1, 2, 3, 4, 5])
print('\n')
skrivsekvens('abcdefg')
print('\n')


# Oppgave 3
def renteutvikling(start, rentesats, slutt):
    print("Startbeløp:", start, "\nRentesats:", rentesats, "\nØnsket beløp:", slutt)
    i = start
    y = 1
    while i < slutt:
        i = i + i * (rentesats / 100)
        print("år", y, ":", '%.2f' % i)
        y += 1


renteutvikling(1000, 3, 1200)
print('\n')


# Oppgave 4
def gangetabell():
    tabell = """\
      | 1  2  3  4  5  6  7  8  9
    --+---------------------------
    1 | 1  2  3  4  5  6  7  8  9
    2 | 2  4  6  8 10 12 14 16 18
    3 | 3  6  9 12 15 18 21 24 27
    4 | 4  8 12 16 20 24 28 32 36
    5 | 5 10 15 20 25 30 35 40 45
    6 | 6 12 18 24 30 36 42 48 54
    7 | 7 14 21 28 35 42 49 56 63
    8 | 8 16 24 32 40 48 56 64 72
    9 | 9 18 27 36 45 54 63 72 81
    """
    print(tabell)


gangetabell()
