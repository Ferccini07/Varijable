"""
Kamen-Škare-PapirPogodi broj
Napravite program koji će vam omogućiti igranje igre protiv računala -kamen, škare, papir
"""
import random

izbor_racunalo = random.randint(1, 3)

game_running = True
while True:
    izbor_racunalo = 3

    izbor_igrac = int(input("Odaberite kamen (1), škare (2) ili papir (3): "))

    if izbor_racunalo == izbor_igrac:
        print(
            f"Računalo bira {izbor_racunalo}, a igrač {izbor_igrac}. Izjednačeno je. Igraj ponovno.")
        odabir = input(
            "Želiš li igrati ponovno? Odaberi 'da' ili 'ne': ").lower()
        if odabir == 'da':
            continue
        elif odabir == 'ne':
            break
        else:
            print("Unijeli ste pogrešan unos.")

    elif (izbor_racunalo == 1 and izbor_igrac == 2) or (izbor_racunalo == 2 and izbor_igrac == 3) or ((izbor_racunalo == 3 and izbor_igrac == 1)):
        print(
            f"Računalo bira {izbor_racunalo}, a igrač {izbor_igrac}. Računalo pobjeđuje.")
        odabir = input(
            "Želiš li igrati ponovno? Odaberi 'da' ili 'ne': ").lower()
        if odabir == 'da':
            continue
        elif odabir == 'ne':
            break
        else:
            print("Unijeli ste pogrešan unos.")

    elif (izbor_racunalo == 1 and izbor_igrac == 3) or (izbor_racunalo == 2 and izbor_igrac == 1) or ((izbor_racunalo == 3 and izbor_igrac == 2)):
        print(
            f"Računalo bira {izbor_racunalo}, a igrač {izbor_igrac}. Igrač pobjeđuje.")
        odabir = input(
            "Želiš li igrati ponovno? Odaberi 'da' ili 'ne': ").lower()
        if odabir == 'da':
            continue
        elif odabir == 'ne':
            game_running = False
        else:
            print("Unijeli ste pogrešan unos.")

    else:
        print("Unijeli ste pogrešan unos.")
        continue
