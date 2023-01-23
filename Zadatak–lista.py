tip_akorda = input("Unesi tip akorda: dur ili mol: ")
# tip_akorda = "dur"

lista_tonova = ["C", "C#", "D", "D#", "E",
                "F", "F#", "G", "G#", "A", "A#", "H"]
n = len(lista_tonova)

prvi_ton = input(f"Unesi prvi ton iz liste {lista_tonova}: ")
# prvi_ton = "C"

lista_akord = [prvi_ton]

if tip_akorda == "dur":
    lista_akord.append(lista_tonova[(lista_tonova.index(prvi_ton) + 3) % n])
    lista_akord.append(lista_tonova[(lista_tonova.index(prvi_ton) + 6) % n])

if tip_akorda == "mol":
    lista_akord.append(lista_tonova[(lista_tonova.index(prvi_ton) + 2) % n])
    lista_akord.append(lista_tonova[(lista_tonova.index(prvi_ton) + 6) % n])

print(lista_akord)
