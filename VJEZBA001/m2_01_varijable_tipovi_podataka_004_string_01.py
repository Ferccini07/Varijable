"""
MODUL   Modul 2 - Osnove programiranja u Pythonu
TEMA    Varijable i tipovi podataka
NASLOV  STRING - Tekstualni tip podataka
"""

ime = "Petar"
prezime = "Peric"
puno_ime = ime + ' ' + prezime
print(puno_ime)

# nacin pisanja slican pisanju recenice
# 1. korak - napiemo recenicu koju zelimo imati za tekst
'Puno ime i prezime je: Petar peric'
# 2. korak - nakon zadnjeg navodnika bez razmaka dodajemo tocko i iza toga pisemo format()
'Puno ime i prezime je: Petar peric'.format()
# 3. korak - iz teksta izbrisemo vrijednosti koje zelimo zamijenit s varijablom i umjesto toga sttavimo vitice i
#  zatim dodamo te varijable po redu u format
'Puno ime i prezime je: {} {}'.format(ime, prezime)

puno_ime = 'Puno ime i prezime je: {} {}'.format(ime, prezime)
print(puno_ime)

# postoji i kraci nacin - F-strings
puno_ime = f'Puno ime i prezime je: {ime} {prezime}'
print(puno_ime)

# input(f"{ime} upisi svoje prezime: ")

tekst = "Puno \ ime \"i\" prezime"
print(tekst)

naziv_filma = 'Snatch'
godina_objavljivanja = 2000
autor = 'Guy Richie'
prosjecna_ocjena = 8.2
dobitnik_oscara = False
print(f'Film {naziv_filma} objavljen je {godina_objavljivanja}. godine, autor je {autor}, a prosječna ocjena mu je {prosjecna_ocjena}. Dobitnik Oscara: {dobitnik_oscara}')
