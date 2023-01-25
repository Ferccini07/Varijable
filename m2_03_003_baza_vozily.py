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

# header row
header_top_row = f"ID\tTip\t\tProizvođač\t\tRegistarska\t\tGodina prve\t\tCijena"
header_bottom_row = f"  \t   \t\t         \t\toznaka\t\t\tregistracije\t\t(EUR)"
header_line = "_" * 110

print(header_top_row, header_bottom_row, sep="\n")
print(header_line)


def print_element(duljina, indeks):
    """
    Funkcija koja na temelju podataka o duljini rijeci koja sacinjava element i
    indeksu elementa pojedine vrijednosti unutar dictionary-ja printa sami element dict-a
    i potreban broj tabova na krjaju
    """
    if duljina < 10 and indeks == 1:
        print(f"{element}", end="\t"*3)
    elif duljina < 5 and indeks == 3:
        print(f"{element}", end="\t"*3)
    elif duljina > 10 and indeks == 0:
        print(f"{element}", end="\t")
    else:
        print(f"{element}", end="\t"*2)


# table body
for kljuc, vrijednost in vozila_firme.items():
    print(f"{kljuc}", end="\t")
    # print(f"{vrijednost}")
    # print(
    #     f"{vrijednost[0]}\t\t{vrijednost[1]}\t\t{vrijednost[2]}\t\t{vrijednost[3]}\t\t{vrijednost[4]}")
    for element in vrijednost:
        duljina1 = len(element)
        indeks1 = vrijednost.index(element)
        print_element(duljina1, indeks1)
        # if len(element) < 10 and vrijednost.index(element) == 1:
        #     print(f"{element}", end="\t\t\t")
        # elif len(element) < 5 and vrijednost.index(element) == 3:
        #     print(f"{element}", end="\t\t\t")
        # elif len(element) > 10 and vrijednost.index(element) == 0:
        #     print(f"{element}", end="\t")
        # else:
        #     print(f"{element}", end="\t\t")
    print()

# Funkcija koja printa tri \t

# Funkcija koja printa dva \t

# Funkcija koja printa element i neki broj \t
