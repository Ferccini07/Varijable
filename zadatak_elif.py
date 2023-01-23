
# Zadatak 1
"""
Kreirajtelistuod 1 do broja30. Ispišitesvebrojevekoji sudjeljivis 3, 6 i9
•
Provjeraje li brojdjeljivs nekimdrugimradimopomoću% (modulo) operanda.
•
15 % 3 NEMA ostatka, odnosnoto je 0 pa je 15 djeljivs 3.
•
16 % 3 je 1, odnosnoNIJE jednak0 pa 16 NIJE djeljivs 3.
"""
# lista = []

# for broj in range(1, 31):
#     lista.append(broj)

# # print(lista)

# for broj in lista:
#     if broj % 3 == 0 and broj % 3 == 0 and broj % 6 == 0:
#         print(f"Broj {broj} je djeljiv s 3,6 ili 9.")
#     else:
#         print("Broj nije dijeljiv s 3,6,9.")


# # zadatak 2
# """
# Napišiteprogram koji provjeravapripada li unesenariječvrsti riječi palindrom.
# •
# Palindromje riječkojase jednakopiše(ičita) s lijevanadesnois desnanalijevo.
# """

# unesena_rijec = input(
#     "Molimo unesite riječ za koju će se provjeriti pripada li vrsti riječi palindrom: ").lower()

# reverse_rijec = unesena_rijec[::-1]
# print(reverse_rijec)

# if unesena_rijec == reverse_rijec:
#     print(f"{unesena_rijec} je palindrom jer obrnutog redoslijeda glasi: {reverse_rijec}.")
# else:
#     print(f"{unesena_rijec} nije palindrom jer obrnutog redoslijeda glasi: {reverse_rijec}.")

# zadatak 3 - lorem ispum

tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.".lower()
tekst_list = tekst.split()

count = 0
lorem_rijec = "lorem"

for rijec in tekst_list:
    if rijec == "lorem":
        count += 1
print(f"Riječ '{lorem_rijec}' se pojavljuje {count} puta")
