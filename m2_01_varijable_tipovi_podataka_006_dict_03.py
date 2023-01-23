"""
MODUL   Modul 2 - osnove programiranja u pythonu
TEMA    Varijable i tiplovi podataka
NASLOV  DICTIONARY - rjecnik
        DODATNE NAREDBE

"""

# help(dict)
vozila_firme = {
    1: ["Kamion", "Iveco", "OS 001 ZZ", "2015", "45.000,00 €"],
    2: ["Kamion", "Iveco", "OS 002 ZZ", "2015", "47.000,00 €"],
    3: ["Tegljač", "MAN", "RI 001 ZZ", "2018", "78.000,00 €"],
    4: ["Tegljač", "MAN", "RI 002 ZZ", "2020", "97.000,00 €"],
    5: ["Kombi", "Mercedes Benz", "ST 001 ZZ", "2013", "12.000,00 €"],
    6: ["Kombi", "Volkswagen", "ST 002 ZZ", "2021", "35.000,00 €"],
    7: ["Dostavno vozilo", "Volkswagen", "ZG 001 ZZ", "2010", "9.000,00 €"],
    8: ["Dostavno vozilo", "Volkswagen", "ZG 002 ZZ", "2010", "9.300,00 €"],
}

# print()
# print("Ispis prije clear")
# for kljuc, vrijednost in vozila_firme.items():
#     print(f"{kljuc}", end="\t")
#     for element in vrijednost:
#         print(f"{element}", end="\t")
#     print()

# vozila_firme.clear()

# print("Ispis nakon clear")
# for kljuc, vrijednost in vozila_firme.items():
#     print(f"{kljuc}", end="\t")
#     for element in vrijednost:
#         print(f"{element}", end="\t")
#     print()


# POP
# print("Ispis prije pop")
# for kljuc, vrijednost in vozila_firme.items():
#     print(f"{kljuc}", end="\t")
#     for element in vrijednost:
#         print(f"{element}", end="\t")
#     print()

# izcabena_vrijednost = vozila_firme.pop(
#     9, "Ne postoji trazeni element u bazi")
# print()
# print("Izbacena vrijenodst je: ", izcabena_vrijednost)
# print()

# print("Ispis nakon pop")
# for kljuc, vrijednost in vozila_firme.items():
#     print(f"{kljuc}", end="\t")
#     for element in vrijednost:
#         print(f"{element}", end="\t")
#     print()

# popitem - izvacuje zadnju dodanu vrijednost
# print("Ispis prije popitem")
# for kljuc, vrijednost in vozila_firme.items():
#     print(f"{kljuc}", end="\t")
#     for element in vrijednost:
#         print(f"{element}", end="\t")
#     print()

# vrijednost = vozila_firme.popitem()
# print()
# print("Izbacena vrijenodst je: ", vrijednost)
# print()

# print("Ispis nakon popitem")
# for kljuc, vrijednost in vozila_firme.items():
#     print(f"{kljuc}", end="\t")
#     for element in vrijednost:
#         print(f"{element}", end="\t")
#     print()

print("Ispis prije popitem")
for kljuc, vrijednost in vozila_firme.items():
    print(f"{kljuc}", end="\t")
    for element in vrijednost:
        print(f"{element}", end="\t")
    print()

# izbaciti zadnja 2 itema iz dicta pomocu popitem
# u ovoj for petlji range govori samo o broju koliko puta zelimo nesto uciniti
# for broj in range(2):
#     vozila_firme.popitem()

# izbaciti prva tri itema iz dicta pomocu for petlje
# u ovoj for petlji range nam govori o broju key-eva dakle konkretno keyevi 1,2,3
# 4 ne jer range ne ukljcuje  zadnji broj
for broj in range(1, 4):
    vozila_firme.pop(broj)

print("Ispis nakon popitem")
for kljuc, vrijednost in vozila_firme.items():
    print(f"{kljuc}", end="\t")
    for element in vrijednost:
        print(f"{element}", end="\t")
    print()
