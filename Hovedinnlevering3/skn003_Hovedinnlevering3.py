import random as ra

# Hovedinnlevering 3
# Sondre Knutsen (skn003)


# Oppgave a)
class WishSolitaire(object):
    def __init__(self):
        self.initialised = False
        self.decks = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': []}
        cards = ["\u2660A", "\u2666A", "\u2663A", "\u2665A", "\u26607", "\u26667", "\u26637", "\u26657",
                 "\u26608", "\u26668", "\u26638", "\u26658", "\u26609", "\u26669", "\u26639", "\u26659",
                 "\u266010", "\u266610", "\u266310", "\u266510", "\u2660J", "\u2666J", "\u2663J", "\u2665J",
                 "\u2660Q", "\u2666Q", "\u2663Q", "\u2665Q", "\u2660K", "\u2666K", "\u2663K", "\u2665K"]

        for key in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            ra.shuffle(cards)
            while len(self.decks[key]) < 4 and len(cards) > 0:
                self.decks[key].append(cards.pop())

    # Start the game
    def start(self):
        print("Trekk to kort (x for å gå tilbake til menyen)")
        self.initialised = True
        self.current_decks()
        self.next_round()

    # next_round lets you choose which decks you wish to draw cards from
    def next_round(self):
        inp = input("Velg bunker: ")[:2].upper()
        if inp == "X":
            menu(self)
        elif inp[0] != inp[1]:
            if inp[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] and inp[1] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                if self.decks[inp[0]][0][1] == self.decks[inp[1]][0][1]:
                    self.draw_cards(inp[0], inp[1])
                else:
                    print("Kortene har ikke samme verdi, trekk på nytt")
                    self.next_round()
        else:
            print("Venligst velg to forskjellige bunker.")
            self.next_round()

    # current_decks prints out the current state of the decks
    def current_decks(self):
        print(" A", "B", "C", "D", "E", "F", "G", "H", sep="   ")
        top_cards = ""
        for key in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            try:
                top_cards += self.decks[key][0]
                top_cards += "  "
            except IndexError:
                top_cards += "[ ]"
                top_cards += "  "
        print(top_cards)
        print(" " + str(len(self.decks['A'])), len(self.decks['B']), len(self.decks['C']), len(self.decks['D']),
              len(self.decks['E']), len(self.decks['F']), len(self.decks['G']), len(self.decks['H']), sep="   ")

    # draw_cards removes the first card from deck_1 and deck_2
    def draw_cards(self, deck_1, deck_2):
        self.decks[deck_1].pop(0)
        self.decks[deck_2].pop(0)

        top_cards = []
        deck_sizes = 0
        for key in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            deck_sizes += len(self.decks[key])
            try:
                top_cards.append(self.decks[key][0][1])
            except IndexError:
                pass

        if deck_sizes == 0:
            print("Alle bunkene er tomme!")
            menu(self)
        elif len(top_cards) != len(set(top_cards)):
            self.current_decks()
            self.next_round()
        else:
            self.current_decks()
            print("Ingen mulige trekk!")
            menu(self)

    # Oppgave b)
    def save(self):
        print("Skriv filnavn")
        filename = input("filnavn>").lower()
        open(filename + ".txt", "w", encoding="utf-8").close()
        output = ""
        for key in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            for i in range(len(self.decks[key])):
                output += self.decks[key][i]
                output += " "
            output += '\n'
        file = open(filename + ".txt", "w", encoding="utf-8")
        file.write(output)
        file.close()
        print("Game saved!")
        menu()

    # Oppgave c)
    def load(self):
        print("Skriv filnavn")
        filename = input("filnavn>").lower()
        file = open(filename + ".txt", "r", encoding="utf-8")
        lines = file.readlines()
        file.close()

        self.decks = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': []}
        line_num = 0
        for key in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            cards = lines[line_num].split()
            for card in cards:
                self.decks[key].append(card)
            line_num += 1
        print("Game loaded!")
        self.start()


def menu(game=WishSolitaire()):
    if not game.initialised:
        print("""1 - Start nytt spill
2 - Lagre spillet
3 - Last inn lagret spill
4 - Avslutt
Velg handling (0 for meny)""")
    else:
        print("""1 - Start nytt spill
2 - Lagre spillet
3 - Last inn lagret spill
4 - Avslutt
5 - Fortsett
Velg handling (0 for meny)""")
    inp = input("Velg>")
    if inp == "1":
        game.__init__()
        game.start()
    elif inp == "2":
        game.save()
    elif inp == "3":
        game.load()
    elif inp == "4":
        print("Takk for nå!")
        return
    elif inp == "5" and game.initialised:
        game.start()
    else:
        menu()


menu()
