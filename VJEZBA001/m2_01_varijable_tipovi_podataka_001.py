# ime = "Borna"
# prezime = "Fercec"
# godina_rodenja = 1991
# drzava_rodenja = "Hrvatska"
# status_radnog_odnosa = "zaposlen"
# tezina_kg = 81
# spol = "musko"

# stranica_a_cetverokuta = 5
# stranica_b_cetverokuta = 4
# povrsina_cetverokuta = stranica_a_cetverokuta * stranica_b_cetverokuta
# print(povrsina_cetverokuta)

# # Izracun opsega i povrsine trokuta
# stranica_a = 5
# visina_a = 4
# opseg_trokuta = 3 * stranica_a
# print(opseg_trokuta)

# povrsina_trokuta = (stranica_a * visina_a) / 2
# print(povrsina_trokuta)

# snaga = 1.3  # kW
# cijena_struje = 0.95  # kn / kWh
# mjesecna_potrosnja = (snaga * 30 * 2)
# print(mjesecna_potrosnja)


# # Hardcoded tekst koristimo za tekst i poruke koje necemo mijenjati tijekom izvrsavanja programa
# print("Petar")

# # Drugi print ce ispšisivati vrijednost varijable koja god to vrijednost bila pohranjena u varijabli
# print(ime)

# # Ispisimo na ekran ime petar i vrijednost varijeble "ime" s jednim praznim redom izmedju njih
# print("Petar")
# print()
# print(ime)

# # zadatak: ako vrijedi gorsnji opis, kako onda mozemo ispisati ime i prezime hardcoded i pomoću varijabli
# print("Petar Peric")
# print("Petar" + " Peric")
# print("Petar", "Peric")
# print(ime, " ", prezime, ".", sep="")
# print("Petar" + " Peric" + ".")


# zadatak: iSPISATI NA EKRAN SVE PODATKE O OSOBI koristeci prethodno nauceno
# svaki podatak treba biti u svojm redu osim imena i prezimena.
# za podatke za koje je potrebnom, dodajte mjernu jedinicu
# podatke o osobi uzmite iz pteethodnih primjera
# nap: za sada ignorirajte ispis vrijednosti iz varijable zaposlen.

# ime = "Borna"
# prezime = "Fercec"
# godina_rodenja = 1991
# drzava_rodenja = "Hrvatska"
# zaposlen = True
# tezina_kg = 81
# spol = "musko"

# print(ime, end="")
# print("", prezime)
# print(godina_rodenja)
# print(drzava_rodenja)
# print(tezina_kg, "kg")
# print(spol)

# naziv = "Snatch"
# godina_objavljivanja = 2000
# autor_ime = "Guy"
# autor_prezime = "Richie"
# prosjecna_ocjena = 8.2
# dobitnik_Oskara = False

# print(naziv)
# print(autor_ime, end="")
# print("", autor_prezime)
# print(prosjecna_ocjena)
# print(godina_objavljivanja)


# stranica_a_cetverokuta = 5
# stranica_b_cetverokuta = 4
# povrsina_cetverokuta = stranica_a_cetverokuta * stranica_b_cetverokuta
# print(povrsina_cetverokuta)

# print(
#     f"Površina četverokuta stranica {stranica_a_cetverokuta} m i {stranica_b_cetverokuta} m iznosi: {povrsina_cetverokuta} m^2.")
# print(
#     "Površina četverokuta stranica ", stranica_a_cetverokuta, " m i ", stranica_b_cetverokuta, " m iznosi: ", povrsina_cetverokuta, " m^2.", sep="")

# ZADATAK: Obračunska jedinica za potrošnja električne energije je kilovat sat i označava se 1 kWh.
# Predstavlja umnožak snage trošila/uređaja izražene u kilovatima (kW)
# i vremena koje se taj uređaj koristi izraženog u satima (h). kW * h
# Ako je snaga mikrovalne pećnice 1.3 kW, a cijena el. energije za 1 kWh je 0.95 kn,
# koliko kuna, mjesečno, košta uporaba mikrovalne pećnice, ako se koristi 2 sata dnevno?
# Zbog jednostavnosti zaokružimo svaki mjesec na 30 dana
# Ispišite trošak bez i s uračunatim PDV-om.

# snaga = 1.3  # kW
# cijena = 0.95  # kn po kWh
# utrosak_po_danu = 2  # h
# trosak = snaga * cijena * 30 * utrosak_po_danu
# trosak_pdv = trosak * 1.25

# snaga = float(input("Upišite snagu trošila: "))
# cijena = float(input("Upišite cijenu po h: "))
# utrosak_po_danu = int(input("Upišite utrošak po danu: "))

# trosak = snaga * cijena * 30 * utrosak_po_danu
# trosak_pdv = trosak * 1.25

# print("Trošak bez PDV-a iznosi:", trosak, "kn.")
# print("Trošak sa PDV-om iznosi:", trosak_pdv, "kn.")

# ZADAĆA
# Kreirajte varijable (imenujte ih i dodijelite im odgovarajuću vrijednost) te ispišite na ekran odgovarajuće vrijednosti, za:
# Ako automobil troši 5.3 litara na 100 km i ako je cijena goriva 9.56 kn po litri (nije važno kojeg goriva), izračunajte koliko košta 1 km vožnje automobilom. Prikažite mjesečni trošak (30 dana) odlaska na posao automobilom koji je udaljen 20 km u jednom smjeru.
# Imate 10000 kn i možete zaboraviti na njih na 15 godina. Ako Vam banka nudi 2.5% godišnju kamatu za taj iznos, koliko ćete zaraditi nakon 15 godina. Jednostavni kamatni račun k = C * p * t
# k = iznos kamata odnosno prinos
# C = iznos glavnice
# p = godišnja kamatna stopa – NAPOMENA: 5% = 5 / 100 = 0.05
# t = vrijeme u godinama

# a = int(input("Upisite prvi broj: "))
# b = int(input("Upisite drugi broj: "))

# print(a, "+", b, "=", a+b)
# print(a, "-", b, "=", a-b)
# print(a, "*", b, "=", a*b)
# print(a, "/", b, "=", a/b)
# print(a, "**", b, "=", a**b)
# print(a, "%", b, "=", a % b)


a = 192
b = 168
c = 0
d = 184

print(a, ".", b, ".", c, ".", d, sep="")
print(bin(a), ".", bin(b), ".", bin(c), ".", bin(d), sep="")
print(hex(a), ".", hex(b), ".", hex(c), ".", hex(d), sep="")
print(oct(a), ".", oct(b), ".", oct(c), ".", oct(d), sep="")
