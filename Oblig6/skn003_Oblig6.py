# Hovedinnlevering 1
# Sondre Knutsen (skn003)

Emner = []
FagKoder = []
Karakterer = []


def start():
    menu()


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
    enterInput()


def enterInput():
    num = input("Velg handling (0 for meny)> ")
    if num == '0':
        menu()
    elif num == '1':
        emneListe()
    elif num == '2':
        nyttEmne()
    elif num == '3':
        settKarakter()
    elif num == '4':
        karakterSnitt()
    elif num == '5':
        print('Takk for nå')
        return
    else:
        enterInput()


# 1 Emneliste
def emneListe():
    print("Velg fag og/eller emnenivå (<enter> for alle)")
    fag = input(" - Fag: ").strip()
    level = input(" - Emnenivå: ").strip()
    for emne in Emner:
        if (fag == '' or fag == emne[:-3]) and (level == '' or level[0] == emne[-3]):
            karakter = ''
            for k in Karakterer:
                if emne == k[0]:
                    karakter = k[1]

            print(emne, karakter)

    enterInput()


# 2 Legg til emne
def nyttEmne():
    emne = input(" - Emnekode: ").strip().upper()
    if len(emne) > 6 and emne[-3] in ['1', '2', '3']:
        exists = False
        for fag in FagKoder:
            if str.upper(fag[1]) == emne[:-3]:
                exists = True

        if exists and emne not in Emner:
            Emner.append(emne)
        elif not exists:
            fagnavn = input("Fag er ikke registrert!\n - Venligst skriv fagnavn: ").strip()
            FagKoder.append([fagnavn, emne[:-3]])
            Emner.append(emne)

        enterInput()
    else:
        print("Emnekode er ikke gyldig")
        enterInput()


# 3 Sett karakter
def settKarakter():
    emne = input(" - Emnekode: ").strip().upper()
    if emne in Emner:
        karakter = input(" - Karakter (<enter> for å slette): ").strip().upper()
        if karakter == "":
            toDelete = []
            for k in Karakterer:
                if k[0] == emne:
                    toDelete = k

            Karakterer.remove(toDelete)
        elif not karakter in ['A', 'B', 'C', 'D', 'E', 'F'] or len(karakter) > 1:
            print("Ikke gyldig karakter!")
            enterInput()

        exists = False
        for k in Karakterer:
            if k[0] == emne:
                k[1] = karakter
                exists = True

        if exists:
            Karakterer.append([emne, karakter])

        enterInput()
    else:
        print("Emne finnes ikke i emnelisten!")
        enterInput()


# 4 Karaktersnitt
def karakterSnitt():
    print("Velg fag og/eller emnenivå (<enter> for alle)")
    fag = input(" - Fag: ").strip()
    level = input(" - Emnenivå: ").strip()
    areas = []
    for f in FagKoder:
        if fag == '' or fag.lower() == f[0].lower() or fag.upper() == f[1]:
            areas.append(f)

    if len(areas) == 0:
        print("Fag ble ikke funnet!")
        enterInput()
    else:
        grades = []
        for pair in Karakterer:
            for f in areas:
                if (f[1] == pair[0][:-3]) and (level == '' or level[0] == pair[0][-3]):
                    grades.append(pair[1])

        if len(grades) == 0:
            print("Ingen karakterer ble funnet!")
            enterInput()
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
            avgGrade = ''
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
            enterInput()


FagKoder.append(['informasjonsvitenskap', 'INFO'])
FagKoder.append(['økonomi', 'ECON'])
FagKoder.append(['geografi', 'GEO'])

Emner.append('INFO100')
Emner.append('INFO104')
Emner.append('INFO125')
Emner.append('INFO132')
Emner.append('INFO180')
Emner.append('INFO216')
Emner.append('INFO282')
Emner.append('INFO284')
Emner.append('ECON100')
Emner.append('ECON110')
Emner.append('ECON218')
Emner.append('GEO100')
Emner.append('GEO113')
Emner.append('GEO124')

Karakterer.append(['INFO100', 'C'])
Karakterer.append(['INFO104', 'B'])
Karakterer.append(['INFO125', 'B'])
Karakterer.append(['INFO132', 'A'])
Karakterer.append(['INFO216', 'A'])
Karakterer.append(['INFO282', 'C'])
Karakterer.append(['ECON100', 'C'])
Karakterer.append(['ECON110', 'C'])
Karakterer.append(['GEO113', 'D'])
Karakterer.append(['GEO124', 'D'])

start()
