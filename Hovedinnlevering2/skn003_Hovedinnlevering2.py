# Hovedinnlevering 2
# Sondre Knutsen (skn003)


# Oppgave 1
Emner = []
EmnerNy = []

FagKoder = []
FagKoderNy = []

Karakterer = []
KaraktererNy = []


class Emne:
    def __init__(self, emne):
        self.emne = emne

    def add_to_list(self):
        Emner.append(self)
        EmnerNy.append(self)

    def to_text(self):
        return self.emne


class FagKode:
    def __init__(self, fag, kode):
        self.fag = fag
        self.kode = kode

    def add_to_list(self):
        FagKoder.append(self)
        FagKoderNy.append(self)

    def to_text(self):
        return self.fag + ' ' + self.kode


class Karakter:
    def __init__(self, emne, karakter):
        self.emne = emne
        self.karakter = karakter

    def add_to_list(self):
        Karakterer.append(self)
        KaraktererNy.append(self)

    def to_text(self):
        return self.emne.to_text() + ' ' + self.karakter


def start():
    def read_emner():
        file = open('emner.txt', 'r')
        text = file.readlines()
        file.close()
        for e in text:
            emne = Emne(e)
            emne.add_to_list()

    def read_fag():
        file = open('fagkoder.txt', 'r')
        text = file.readlines()
        file.close()
        for t in text:
            f = t.split()
            fagKode = FagKode(f[0], f[1])
            fagKode.add_to_list()

    def read_karakterer():
        file = open('karakterer.txt', 'r')
        text = file.readlines()
        file.close()
        for t in text:
            k = t.split()
            emne = Emne(k[0])
            karakter = Karakter(emne, k[1])
            karakter.add_to_list()

    read_emner()
    read_fag()
    read_karakterer()

    menu()


def avslutt():
    def write_emner():
        file = open('emner.txt', 'w')
        for e in EmnerNy:
            ln = e.to_text() + '\n'
            file.write(ln)
        file.close()

    def write_fag():
        file = open('fagkoder.txt', 'w')
        for f in FagKoderNy:
            ln = f.to_text() + '\n'
            file.write(ln)
        file.close()

    def write_karakterer():
        file = open('karakterer.txt', 'w')
        for k in KaraktererNy:
            ln = k.to_text() + '\n'
            file.write(ln)
        file.close()

    response = input("Ønsker du å lagre endringene?(j/n) >")
    if response.lower() == 'j':
        write_emner()
        write_fag()
        write_karakterer()
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
        elif karakter not in ['A', 'B', 'C', 'D', 'E', 'F'] or len(karakter) > 1:
            print("Ikke gyldig karakter!")
            enter_input()

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
            self.tilgang.append(a.kode)


class Kontor:
    def __init__(self, nr):
        self.nr = nr
        self.tilgang = []
        self.eier = None
        Rom.append(self)

    def skriv(self):
        print(self.nr, self.tilgang, '\n -', self.eier)

    def sett_eier(self, eier):
        self.eier = eier
        self.tilgang.append(eier.kode)
