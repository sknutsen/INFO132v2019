# Temainnlevering 3
# Sondre Knutsen (skn003)

# Oppgave 1
# a)
x = 8
y = 10
statement_1 = x != 7 and y <= 50
statement_2 = (x > 7 or 50 < y) and (x > y or y < 100)

print("x != 7 and y <= 50 =", statement_1, "   (x > 7 or 50 < y) and (x > y or y < 100) =", statement_2)

# b)
statement_1 = not (x == 7 and y > 50)
statement_2 = not (x <= 7 or 50 >= y) and (x > y or y < 100)

print("not (x == 7 and y > 50) =", statement_1, "   (x > 7 or 50 < y) and (x > y or y < 100) =", statement_2)

# Oppgave 2
age = int(input("Oppgi alder: "))
how_long = int(input("Hvor lenge har du bodd i Tulleby? "))
mayor = age >= 30 and how_long >= 9
council = age >= 25 and how_long >= 5
mayor_years_left = 0
council_years_left = 0
if 30 - age > 9 - how_long:
    mayor_years_left = 30 - age
else:
    mayor_years_left = 9 - how_long

if 25 - age > 5 - how_long:
    council_years_left = 25 - age
else:
    council_years_left = 5 - how_long

if mayor:
    print("Du kan bli ordfører eller sitte i bystyret")
elif not mayor and council:
    print("Du kan sitte i bystyret\nPrøv igjen om", mayor_years_left, "år for å bli ordfører")
else:
    print("Du er ikke kvalifisert enda, prøv igjen om", council_years_left, "år")

# Oppgave 3
x = int(input('tall:'))
if 5 < x < 10:
    print('6,7,8 eller 9')
elif x >= 10:
    print('minst 10')
else:
    print('max 5')
