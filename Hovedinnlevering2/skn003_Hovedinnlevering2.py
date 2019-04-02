# Hovedinnlevering 2
# Sondre Knutsen (skn003)


# Oppgave 1
Emner = []

FagKoder = []

Karakterer = []


class Emne:
    def __init__(self, emne):
        self.emne = emne

    def add_to_list(self):
        Emner.append(self)

    def in_list(self):
        for e in Emner:
            if e.emne == self.emne:
                return True
        return False

    def get_fag(self):
        for f in FagKoder:
            if f.kode == self.emne[:-3]:
                return f.to_text()
        return ''

    def to_text(self):
        return self.get_fag() + ' ' + self.emne


class FagKode:
    def __init__(self, fag, kode):
        self.fag = fag
        self.kode = kode

    def add_to_list(self):
        FagKoder.append(self)

    def in_list(self):
        for f in FagKoder:
            if f.fag == self.fag:
                return True
        return False

    def to_text(self):
        return self.fag


class Karakter:
    def __init__(self, emne, karakter):
        self.emne = emne
        self.karakter = karakter

    def add_to_list(self):
        Karakterer.append(self)

    def in_list(self):
        for k in Karakterer:
            if k.emne.emne == self.emne.emne:
                return True
        return False

    def to_text(self):
        return self.emne.to_text() + ' ' + self.karakter


def start():
    try:
        file = open('emneInfo.txt', 'r')
    except FileNotFoundError:
        open('emneInfo.txt', 'w').close()
        file = open('emneInfo.txt', 'r')
    text = file.readlines()
    file.close()
    if len(text) > 0:
        for t in text:
            k = t.split()
            emne = Emne(k[1])
            if not emne.in_list():
                emne.add_to_list()
            fagKode = FagKode(k[0], k[1][:-3])
            if not fagKode.in_list():
                fagKode.add_to_list()
            try:
                karakter = Karakter(emne, k[2])
                if not karakter.in_list():
                    karakter.add_to_list()
            except IndexError:
                pass

    menu()


def avslutt():
    def write():
        open('emneInfo.txt', 'w').close()
        file = open('emneInfo.txt', 'w')
        for emne in Emner:
            found = False
            ln = ''
            for k in Karakterer:
                if emne.emne == k.emne.emne:
                    found = True
                    ln = k.to_text() + '\n'
            if not found:
                ln = emne.to_text() + '\n'
            file.write(ln)
        file.close()

    response = input("Ønsker du å lagre endringene?(j/n) >")
    if response.lower() == 'j':
        write()
    print("Takk for nå")


def menu():
    menu_ = '''\n
--------------------
 1 Emneliste
 2 Legg til emne
 3 Sett karakter
 4 Karaktersnitt
 5 Avslutt
--------------------'''
    print(menu_)
    enter_input()


def enter_input():
    num = input("Velg handling (0 for meny)> ")
    if num == '0':
        menu()
    elif num == '1':
        emneliste()
    elif num == '2':
        nytt_emne()
    elif num == '3':
        sett_karakter()
    elif num == '4':
        karaktersnitt()
    elif num == '5':
        avslutt()
    else:
        enter_input()


# 1 Emneliste
def emneliste():
    print("Velg fag og/eller emnenivå (<enter> for alle)")
    fag = input(" - Fag: ").strip()
    level = input(" - Emnenivå: ").strip()
    for emne in Emner:
        if (fag == '' or fag == emne.emne[:-3]) and (level == '' or level[0] == emne.emne[-3]):
            karakter = Karakter('', '')
            for k in Karakterer:
                if emne.emne == k.emne.emne:
                    karakter = k

            print(emne.emne, karakter.karakter)

    enter_input()


# 2 Legg til emne
def nytt_emne():
    emne = input(" - Emnekode: ").strip().upper()
    if len(emne) >= 6 and emne[-3] in ['1', '2', '3']:
        exists = False
        for fag in FagKoder:
            if str.upper(fag.kode) == emne[:-3]:
                exists = True

        if exists and emne not in Emner:
            nyttemne = Emne(emne)
            nyttemne.add_to_list()
        elif not exists:
            fagnavn = input("Fag er ikke registrert!\n - Venligst skriv fagnavn: ").strip()
            FagKoder.append(FagKode(fagnavn, emne[:-3]))
            nyttemne = Emne(emne)
            nyttemne.add_to_list()

        enter_input()
    else:
        print("Emnekode er ikke gyldig")
        enter_input()


# 3 Sett karakter
def sett_karakter():
    emnenavn = input(" - Emnekode: ").strip().upper()
    emne = Emne('')
    for e in Emner:
        if e.emne == emnenavn:
            emne = e
    if emne.emne != '':
        karakter = input(" - Karakter (<enter> for å slette): ").strip().upper()
        if karakter == "":
            toDelete = Karakter
            for k in Karakterer:
                if k.emne == emne:
                    toDelete = k

            Karakterer.remove(toDelete)
            print('Karakter slettet!')
            enter_input()
        elif karakter not in ['A', 'B', 'C', 'D', 'E', 'F'] or len(karakter) > 1:
            print("Ikke gyldig karakter!")
            enter_input()
        else:
            nyKarakter = Karakter(emne, karakter)
            exists = False
            for i in range(len(Karakterer)):
                if Karakterer[i].emne == emne:
                    Karakterer[i] = nyKarakter
                    exists = True

            if not exists:
                nyKarakter.add_to_list()

            enter_input()
    else:
        print("Emne finnes ikke i emnelisten!")
        enter_input()


# 4 Karaktersnitt
def karaktersnitt():
    print("Velg fag og/eller emnenivå (<enter> for alle)")
    fag = input(" - Fag: ").strip()
    level = input(" - Emnenivå: ").strip()
    areas = []
    for f in FagKoder:
        if fag == '' or fag.lower() == f.fag.lower() or fag.upper() == f.kode.upper():
            areas.append(f)

    if len(areas) == 0:
        print("Fag ble ikke funnet!")
        enter_input()
    else:
        grades = []
        for k in Karakterer:
            for f in areas:
                if (f.kode == k.emne.emne[:-3]) and (level == '' or level[0] == k.emne.emne[-3]):
                    grades.append(k.karakter)

        if len(grades) == 0:
            print("Ingen karakterer ble funnet!")
            enter_input()
        else:
            a = 0
            b = 0
            c = 0
            d = 0
            e = 0
            for grade in grades:
                if str(grade).lower() == 'a':
                    a += 6
                elif str(grade).lower() == 'b':
                    b += 5
                elif str(grade).lower() == 'c':
                    c += 4
                elif str(grade).lower() == 'd':
                    d += 3
                elif str(grade).lower() == 'e':
                    e += 2

            avg = (a + b + c + d + e) / len(grades)
            if int(avg) == 2:
                avgGrade = 'E'
            elif int(avg) == 3:
                avgGrade = 'D'
            elif int(avg) == 4:
                avgGrade = 'C'
            elif int(avg) == 5:
                avgGrade = 'B'
            elif int(avg) == 6:
                avgGrade = 'A'
            else:
                avgGrade = 'F'
            print("Snitt:", avgGrade)
            enter_input()


start()


# Oppgave 2
Ansatte = []
Rom = []


class Ansatt:
    def __init__(self, navn, kode):
        self.navn = navn
        self.kode = kode
        Ansatte.append(self)

    def skriv(self):
        print(self.navn, self.kode)


class Vaktmester(Ansatt):
    def gi_tilgang(self):
        for r in Rom:
            if self.kode not in r.tilgang:
                r.tilgang.append(self.kode)


class Møterom:
    def __init__(self, nr, kapasitet):
        self.nr = nr
        self.tilgang = []
        self.kapasitet = kapasitet
        Rom.append(self)

    def skriv(self):
        print(self.nr, self.tilgang, '\n -', self.kapasitet)

    def sett_koder(self):
        for a in Ansatte:
            if a.kode not in self.tilgang:
                self.tilgang.append(a.kode)

    def åpne(self, kode):
        if kode in self.tilgang:
            print("Rom", self.nr, "er åpent.")
            return True
        else:
            print("Feil kode.")
            return False


class Kontor:
    def __init__(self, nr):
        self.nr = nr
        self.tilgang = []
        self.eier = None
        Rom.append(self)

    def skriv(self):
        if self.eier is not None:
            print(self.nr, self.tilgang, '\n -', self.eier.navn)
        else:
            print(self.nr, self.tilgang)

    def sett_eier(self, eier):
        old = self.eier
        if old is not None:
            self.tilgang.remove(old.kode)
        self.eier = eier
        self.tilgang.append(eier.kode)

    def åpne(self, kode):
        if kode in self.tilgang:
            print("Rom", self.nr, "er åpent.")
            return True
        else:
            print("Feil kode.")
            return False


m1 = Møterom(1, 10)
m2 = Møterom(2, 20)
k1 = Kontor(3)
k2 = Kontor(4)
k3 = Kontor(5)
kari = Ansatt('Kari', 1111)
ole = Ansatt('Ole', 2222)
trond = Vaktmester('Trond', 3333)
k1.sett_eier(kari)
k2.sett_eier(ole)
k3.sett_eier(trond)
trond.gi_tilgang()
k1.åpne(kari.kode)
k1.åpne(ole.kode)
for a in Ansatte:
    a.skriv()
for r in Rom:
    r.skriv()
