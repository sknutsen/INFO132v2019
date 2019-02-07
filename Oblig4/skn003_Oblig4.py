import math as m


# Temainnlevering 4
# Sondre Knutsen (skn003)

# Oppgave 1
# a)
def pi(d):
    if d <= len(str(m.pi)) - 2:
        print(("{0:." + str(d) + "f}").format(m.pi))
    elif d > len(str(m.pi)) - 2:
        print("For mange desimaler!", m.pi, sep="\n")


pi(13)


# b)
def pi():
    print("{0:.2f}".format(m.pi))


# Oppgave 2
# a)
