vozila_firme = {
    1: ["Kamion", "Iveco", "OS 001 ZZ", "2015", "45.000,00 €"],
    2: ["Kamion", "Iveco", "OS 002 ZZ", "2015", "47.000,00 €"],
    3: ["Tegljač", "MAN", "RI 001 ZZ", "2018", "78.000,00 €"],
    4: ["Tegljač", "MAN", "RI 002 ZZ", "2020", "97.000,00 €"],
    5: ["Kombi", "Mercedes Benz", "ST 001 ZZ", "2013", "12.000,00 €"],
    6: ["Kombi", "Volkswagen", "ST 001 ZZ", "2021", "35.000,00 €"],
    7: ["Dostavno vozilo", "Volkswagen", "ZG 001 ZZ", "2010", "9.000,00 €"],
    8: ["Dostavno vozilo", "Volkswagen", "ZG 001 ZZ", "2010", "9.300,00 €"],
}

print("ID", sep="\t", end="\t")
naslovi = ["Tip", "Proizvođač", "Registarska oznaka",
           "Godina prve registracije", "Cijena u EUR"]
for item in naslovi:
    print(item, end="\t\t")

for key, item in vozila_firme.items():
    print(key, end="\t")
    for i in range(5):
        if item[i] == "Dostavno vozilo":
            print(item[i], end="\t")
        else:
            print(item[i], end="\t\t")
    print("\n")
