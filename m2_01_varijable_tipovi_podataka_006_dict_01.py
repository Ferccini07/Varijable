"""
MODUL   Modul 2 - osnove programiranja u pythonu
TEMA    Varijable i tiplovi podataka
NASLOV  DICTIONARY - rjecnik

"""
# stanovnistvo_lista = ['Petar Peric', 'Marko Maric',
# 'Ivan Ivic', 'Josip Josipovic', 'Marko Maric']

stanovnistvo = {
    '12342132131': "Petar Peric", "12342222131": 'Marko Maric',
    "21654343": 'Ivan Ivic', "1545438763": 'Josip Josipovic', "6786738": 'Marko Maric'}

# 'Hrvoje Horvat'

# dohvacanje vriejdnosti iz rijecnika pomocu kljuca
# print(stanovnistvo["12342222131"])

# # dodavanje novog para vrijednost-kkljuc u rijecnik
# stanovnistvo["5435434"] = 'Hrvoje Horvat'

# # pregaziti vrijednsot pod odredenim kljucem
# stanovnistvo["12342132131"] = 'Petar Pericic'

# print(stanovnistvo)

# for petlja za dict

# ispisati sve kljuceve iz rijecnika

for key in stanovnistvo.keys():
    print(key)

for value in stanovnistvo.values():
    print(value)

# # ili

for key in stanovnistvo.keys():
    print(stanovnistvo[key])

for item in stanovnistvo.items():
    print(item)

for key, item in stanovnistvo.items():
    print(key)
    print(value)
    print()

# stanovnistvo = {
#     "12345671": ["Petar", "Peric", 30, "zaposlen"],
#     "12345672": ["Marko", "Maric", 32, "zaposlen"],
#     "12345673": ["Ivan", "Ivic", 27, "nezaposlen"],
#     "12345672": ["Josip", "Josipovic", 42, "zaposlen"],
# }

# print(stanovnistvo)

# #
# # listaa = stanovnistvo["12345671"]
# # print(listaa[1])

# print(stanovnistvo["12345671"][1])
