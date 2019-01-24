import math
import random

# Temainnlevering 2
# sondre knutsen (skn003)

# Oppgave 1
r = input("Radius: ")
area = '%.3f' % (float(r)**2*math.pi)
print("Arealet til en sirkel med radius ", r, " er ", area, "\n", sep="")


# Oppgave 2
string = input("Sentence: ")
guess = input("Guess: ")
print("That's ", str(len(string) == int(guess)), "!!\n", sep="")


# Oppgave 3
n = input("Gi meg et tall: ")
rand = str(random.randint(1, 9))
result = '%.1f' % (int(n + rand) / int(n))
print(n, rand, " / ", n, " = ", result, sep="")
