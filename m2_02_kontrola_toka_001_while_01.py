"""
MODUL       Modul 2 - Osnove progamiranja u Pythonu
TEMA        Kontrola toka izvrsavanja programskog koda
NASLOV      Uvjetno izvrsavanje programa
            WHILE petlja
"""

brojevi = []
for broj in range(1, 21):
    brojevi.append(broj)

# for petlja
print("FOR petlja")
for broj in brojevi:
    print(broj, end=" ")

print()
print()

# while petlja
print("WHILE petlja")
brojac = 0
while (brojac < len(brojevi)):
    print(brojevi[brojac], end=" ")
    brojac += 1

# if petlja
print("IF petlja")
if brojac < len(brojevi):
    print(brojevi[brojac], end=" ")
    brojac += 1

while True:
    print("Bok")
