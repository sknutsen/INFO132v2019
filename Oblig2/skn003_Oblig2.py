import math
import random

# Temainnlevering 2
# sondre knutsen (skn003)

# Oppgave 1
r = input("Radius: ")
print("Arealet til en sirkel med radius", r, "er " + '%.3f' % (float(r)**2*math.pi))


# Oppgave 2
string = input("Sentence: ")
guess = input("Guess: ")
print("That's", str(len(string) == int(guess)) + "!!\n")


# Oppgave 3
n = input("Gi meg et tall: ")
rand = str(random.randint(1, 9))
print(n + rand + "/" + n + "=" + '%.1f' % (int(n + rand) / int(n)))
