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


pi(5)
pi(12)
pi(30)
print("\n")


# b)
def pi():
    print("{0:.2f}".format(m.pi))


pi()
print('\n')


# Oppgave 2
# a)
def temperatureConverter(d, u):
    if u == 'C':
        print(d * 1.8 + 32)
    elif u == 'F':
        print((d - 32) / 1.8)


temperatureConverter(34, 'C')
temperatureConverter(93.2, 'F')
print('\n')


# b)
def temperatureConverter(d):
    print(d * 1.8 + 32)


temperatureConverter(34)
print('\n')


# Oppgave 3
saldo = 500
rentesats = 0.1


def innskudd(n):
    global saldo
    global rentesats

    saldo += n

    if saldo >= 1000000:
        rentesats = 0.2
        print('Gratulerer med bonusrenta')


def uttak(n):
    global saldo
    global rentesats

    if n > saldo:
        print('Overtrekk')
        return

    saldo -= n

    if saldo < 1000000:
        rentesats = 0.1
        print('du har nå ordinær rente')


def beregnRente():
    global saldo
    global rentesats

    print(saldo * rentesats)


def renteoppgjør():
    global saldo
    global rentesats

    innskudd(rentesats)


print("Saldo:", saldo)
print("Rentesats:", rentesats)
innskudd(300)
print("Saldo:", saldo)
uttak(100)
print("Saldo:", saldo)
beregnRente()
print("Saldo:", saldo)
renteoppgjør()
print("Saldo:", saldo)
innskudd(1000000)
print("Saldo", saldo)
print("Rentesats:", rentesats)
uttak(500000)
print("Saldo:", saldo)
print("Rentesats:", rentesats)
uttak(1000000)
print("Saldo:", saldo)
