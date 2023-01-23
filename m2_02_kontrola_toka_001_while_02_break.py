"""
MODUL       Modul 2 - Osnove progamiranja u Pythonu
TEMA        Kontrola toka izvrsavanja programskog koda
NASLOV      Uvjetno izvrsavanje programa
            BREAK i CONTINUE za FOR i WHILE petlju
"""

tekst = "Python programer"

# for znak in tekst:
#     print(znak, end=" ")
# print()

# for znak in tekst:
#     if znak == "g":
#         break
#     print(znak, end=" ")
# print()

# while True:
#     print("Pozdrav iz potencijalno beskonacne WHILE petlje")

#     odgovor = int(input("Zelite li prekinuti petlju? (Da=1/Ne=0) "))
#     if odgovor == 1:
#         print("Izlazimo iz petlje")
#         break
#     elif odgovor == 0:
#         print("Ostajemo u petlji.")
#     else:
#         print("Unijeli ste pogresan unos.")

for znak in tekst:
    if znak == 'g':
        continue
    print(znak, end=" ")
print()
