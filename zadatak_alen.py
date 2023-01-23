"""
MODUL   Modul 2 - osnove programiranja u pythonu
TEMA    Varijable i tiplovi podataka
NASLOV  KOLEKCIJE PODATAKA
        ZADATAK AKORDI
"""

tonovi = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A",
          "A#", "H"]

print("Lista svih tonova pocevsi od C: ")
for ton in tonovi:
    print(ton, end="")
print()

pocetni_ton = input("Unesite pocetni ton akorda: \t")


index_pocetnog_tona = tonovi.index(pocetni_ton)

print(index_pocetnog_tona)

print(
    f"{pocetni_ton} Dur akord za pocetni ton cine tonovi {pocetni_ton}, {tonovi[index_pocetnog_tona] + 3}, {tonovi[index_pocetnog_tona] +6}")
