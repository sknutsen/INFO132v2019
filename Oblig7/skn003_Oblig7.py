# Temainnlevering 7
# Sondre Knutsen (skn003)


# Oppgave 1
Eksamen = {'INFO100': 'C', 'INFO104': 'B', 'INFO116': 'E', 'INFO180': 'A', 'INFO201': 'F', 'INFO280': 'C',
           'GEO101': 'D', 'GEO110': 'B', 'ADM101': 'A', 'ECON100': 'B', 'ECON201': 'C', 'GEO210': 'C', 'FAIL101': 'F'}


# Oppgave 1a)
def karakterfrekvenser(di):
    result = {}
    for v in di.values():
        result[v] = list(di.values()).count(v)
    return result


f = karakterfrekvenser(Eksamen)
print('1a)\n', f)


# Oppgave 1b)
def histogram(di):
    for key in sorted(di):
        star = ''
        for n in range(di[key]):
            star += '*'
        print(key, star)


print('\n1b)')
histogram(f)


# Oppgave 2
engelskeSiffer = {1: 'one', 0: 'zero', 2: 'two', 3: 'three', 4: 'four',
                  5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}


# Oppgave 2a)
def skrivSortert(di):
    for key in sorted(di):
        print(key, di[key])


print('\n2a)')
skrivSortert(engelskeSiffer)


# Oppgave 2b)
def invers(di):
    result = {}
    for x in di:
        result[di[x]] = x
    return result


i = invers(engelskeSiffer)
print('\n2b)\n', i)


# Oppgave 2c)
def skrivInversSortert(di):
    temp = invers(di)
    result = {}
    for x in sorted(temp):
        result[temp[x]] = x
    for x in result:
        print(x, result[x])


del engelskeSiffer
print('\n2c)')
skrivInversSortert(i)
