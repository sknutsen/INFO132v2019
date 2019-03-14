# Hovedinnlevering 1
# Sondre Knutsen (skn003)

Emner = []
FagKoder = []
Karakterer = []


def menu():
    menu_ = '''\n
--------------------
 1 Emneliste
 2 Legg til emne
 3 Sett karakter
 4 Karaktersnitt
 5 Karakterliste
 6 Fagkoder
 7 
 8 
 9 
 0 Avslutt
--------------------'''
    print(menu_)
    enterInput()


def emneliste():
    print(Emner)
    enterInput()


def addEmne():
    emne = input("Emnenavn: ")
    Emner.append(emne)
    enterInput()


def settKarakter():
    emne = input("Emnenavn: ")
    if emne in Emner:
        karakter = input("Karakter: ")
        if karakter.strip() == "":
            return
        elif not karakter.lower() in ['a', 'b', 'c', 'd', 'e', 'f']:
            print("not a valid input!")
            settKarakter()
        Karakterer.append([emne, karakter])
        enterInput()
    else:
        print("Emne finnes ikke i emnelisten!")
        settKarakter()


def karakterSnitt():
    grades = []
    for pair in Karakterer:
        grades.append(pair[1])

    avg = 1 / len(grades)
    print(avg)
    enterInput()


def karakterliste():
    print(Karakterer)
    enterInput()


def fagkoder():
    print(FagKoder)
    enterInput()


def start():
    menu()


def enterInput():
    num = input("Velg handling (0 for meny)> ")
    if num == '0':
        menu()
    elif num == '1':
        emneliste()
    elif num == '2':
        addEmne()
    elif num == '3':
        settKarakter()
    elif num == '4':
        karakterSnitt()
    elif num == '5':
        karakterliste()
    elif num == '6':
        fagkoder()
    elif num == '7':
        return
    elif num == '8':
        return
    elif num == '9':
        return
    elif num == '0':
        return
    else:
        enterInput()


start()
