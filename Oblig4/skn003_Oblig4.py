import math as m


# Temainnlevering 4
# Sondre Knutsen (skn003)

# Oppgave 1
# a)
def pi(d):
    if d <= len(str(m.pi)) - 2:
        print(("{0:." + str(d) + "f}").format(m.pi), '\n')
    elif d > len(str(m.pi)) - 2:
        print("For mange desimaler!", m.pi, sep="\n")


pi(5)
pi(12)
pi(30)
print("\n")


# b)
def pi(d=2):
    if d <= len(str(m.pi)) - 2:
        print(("{0:." + str(d) + "f}").format(m.pi), '\n')
    elif d > len(str(m.pi)) - 2:
        print("For mange desimaler!", m.pi, sep="\n")


pi()
print('\n')


# Oppgave 2
# a)
def temperaturKonvertering(d, u):
    if u == 'C':
        print(d * 1.8 + 32, '\n')
    elif u == 'F':
        print((d - 32) / 1.8, '\n')


temperaturKonvertering(34, 'C')
temperaturKonvertering(93.2, 'F')
print('\n')


# b)
def temperaturKonvertering(d, u='C'):
    if u == 'C':
        print(d * 1.8 + 32, '\n')
    elif u == 'F':
        print((d - 32) / 1.8, '\n')


temperaturKonvertering(34)
print('\n')


# Oppgave 3
saldo = 500
rentesats = 0.01


def innskudd(n):
    global saldo
    global rentesats

    if saldo <= 1000000 < saldo+n:
        saldo += n
        rentesats = 0.02
        print('gratulerer, du får bonusrente')
    else:
        saldo += n


def uttak(n):
    global saldo
    global rentesats

    if n > saldo:
        print('overtrekk')
    else:
        if saldo > 1000000 > saldo-n:
            rentesats = 0.01
            print('du har nå ordinær rente')
        saldo -= n


def beregnrente():
    global saldo
    global rentesats

    print("Rente: ", rentesats * saldo)


def renteoppgjør():
    global saldo
    global rentesats

    saldo = saldo + (rentesats * saldo)
    print(saldo)


print("Saldo:", saldo)
print("\nRentesats:", rentesats)
innskudd(300)
print("\ninnskudd()")
print("Saldo:", saldo)
uttak(100)
print("\nuttak()")
print("Saldo:", saldo)
beregnrente()
print("\nberegnrente()")
print("Saldo:", saldo)
renteoppgjør()
print("\nrenteoppgjør()")
print("Saldo:", saldo)
innskudd(1000000)
print("\ninnskudd()")
print("Saldo:", saldo)
print("\nRentesats:", rentesats)
uttak(500000)
print("\nuttak()")
print("Saldo:", saldo)
print("\nRentesats:", rentesats)
uttak(1000000)
print("\nuttak()")
print("Saldo:", saldo)
