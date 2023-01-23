"""
MODUL       Modul 2 - Osnove progamiranja u Pythonu
TEMA        Kontrola toka izvrsavanja programskog koda
NASLOV      Uvjetno izvrsavanje programa
            IF ELIF ELSE
"""

prvi_uvjet = False
drugi_uvjet = False
treci_uvjet = True
cetvrti_uvjet = True

# if prvi_uvjet:
#     print("Jej prvi uvjet je zadovoljen")
# else:
#     print("Joj prvi uvjet nije zadovoljen")

# if drugi_uvjet:
#     pass
# else:
#     print("Joj prvi uvjet nije zadovoljen")

if prvi_uvjet:
    print("Zadovoljen je prvi uvjet.")
elif drugi_uvjet:
    print("Zadovoljen je drugi uvjet.")
elif treci_uvjet:
    print("Zadovoljen je treci uvjet")
elif cetvrti_uvjet:
    print("Zadovoljen je cetvrti uvjet")
else:
    print("Nije zadovoljen niti jedan uvjet.")
