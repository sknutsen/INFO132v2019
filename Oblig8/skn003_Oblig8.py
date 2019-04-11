# Temainnlevering 8
# Sondre Knutsen (skn003)
import re

# Oppgave 1
Bøker = {('Blackburn', 'Modal logic'): ('logikk', '2002'),
         ('Brook', 'Knowledge and Mind'): ('filosofi', '2000'),
         ('Dowek', 'Computation, proof, machine'): ('matematikk', '2015'),
         ('Dowek', 'Proofs and algorithms'): ('logikk', '2011'),
         ('Hein', 'Discrete mathematics'): ('matematikk', '2003'),
         ('Horstmann', 'Python for everyone'): ('programmering', '2016'),
         ('Lowe', 'A survey of metaphysics'): ('filosofi', '2002'),
         ('Severance', 'Java for somebody'): ('programmering', '1999'),
         ('Severance', 'Python for everybody'): ('programmering', '2016')}


# Oppgave 1a)
def skrivBøker():
    for ((au, t), (ar, y)) in Bøker.items():
        print(au, t, ar, y, sep=', ')


print('1a)')
skrivBøker()


# Oppgave 1b)
def leggTilBok():
    auth = input('Forfatter: ')
    title = input('Tittel: ')
    area = input('Fagfelt: ')
    year = input('Utgivelsesår: ')
    Bøker[(auth, title)] = (area, year)


print('1b)')
leggTilBok()
skrivBøker()


# Oppgave 1c)
def finnForfatter():
    auth = input('Forfatter: ')
    for ((au, t), (ar, y)) in Bøker.items():
        if auth.lower() == au.lower():
            print(t, y, sep=', ')


print('1c)')
finnForfatter()


# Oppgave 1d)
def finnFagområde():
    area = input('Fagområde: ')
    for ((au, t), (ar, y)) in Bøker.items():
        if area.lower() == ar.lower():
            print(au, t, y, sep=', ')


print('1d)')
finnFagområde()


# Oppgave 2
temp = \
    '''Mandag var middeltemperaturen 9.87 grader
    og tirsdag var den 11.0.
    Neste dag var middeltemperaturen 7.987
    mens torsdag var den 8.88. Fredag steg
    temperaturen til 9.7 grader og i helgen
    fikk vi 9.9 og 7.7 grader.'''


# Oppgave 2a)
def tMinst4(text):
    print('2a)')
    words = text.split()
    søk = '^t'
    for w in words:
        if re.search(søk, w) and len(w) >= 4:
            print(w)


# Oppgave 2b)
def ordFørTall(text):
    print('2b)')
    søk = '([a-z]+)\s[0-9]+'
    result = re.findall(søk, text)
    print(result)


tMinst4(temp)
ordFørTall(temp)
