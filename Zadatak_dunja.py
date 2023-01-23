pocetni_ton = input("Unesite početni ton akorda: ")
odabrani_tip_akorda = input(
    "Unesite želite li molski (unesite 'mol') ili durski akord (unesite 'dur'): ")
glazbena_abeceda = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A",
                    "A#", "H", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"]

index_pocetnog_tona = glazbena_abeceda.index(pocetni_ton.upper())
