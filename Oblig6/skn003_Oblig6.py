# Temainnlevering 6
# Sondre Knutsen (skn003)


# Oppgave 1
def addNumber():
    print("Legg til navn og nummer, avslutt med <enter>")
    file = open('telefon.txt', 'r', encoding="utf-8")
    text = file.readlines()
    file.close()
    while True:
        number = input("Navn og nummer: ").strip()
        if number == '':
            file = open('telefon.txt', 'w', encoding="utf-8")
            file.writelines(text)
            file.close()
            break
        else:
            text.append(number + '\n')


# Oppgave 2
def editNumber():
    name = input("Navn: ").strip().lower()
    if name == '':
        return
    file = open('telefon.txt', 'r+', encoding="utf-8")
    text = file.readlines()
    output = []
    file.close()
    for l in text:
        line = l.split()
        if line[0].lower() == name:
            print("Nummer:", line[1])
            newnum = input("Nytt nummer: ").strip()
            output.append(line[0] + ' ' + newnum + '\n')
        else:
            output.append(l)

    file = open('telefon.txt', 'w', encoding="utf-8")
    file.writelines(output)
    file.close()


# Oppgave 3
def removeVowels(filename=''):
    if filename == '':
        filename = input("Filnavn: ").strip()
        if filename == '':
            return

    file = open(filename, 'r')
    text = file.read()
    file.close()
    outputtext = ""
    for c in text:
        if c.lower() not in 'aeiouyæøå':
            outputtext += c

    output = open(filename + "_NY.txt", 'w')
    output.write(outputtext)
    output.close()


addNumber()
editNumber()
removeVowels('treSmåKinesere.txt')
