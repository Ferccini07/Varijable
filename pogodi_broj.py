import random
zamisljeni_broj = random.randint(1, 100)
broj_pokusaja = 0

while True:
    odgovor = int(input("Pogodi broj od 1 do 100 koji sam zamislio.\t"))
    broj_pokusaja += 1

    if odgovor == zamisljeni_broj:
        print("Čestitam! To je broj koji sam zamislio.")
        print(f"Za pogoditi ti je trebalo {broj_pokusaja} pokušaja.")
        print()
        break
    elif odgovor < zamisljeni_broj:
        print(f"Zamišljeni broj je veći od {odgovor}.")
    else:
        print(f"Zamišljeni broj je manji od {odgovor}.")
