

rijec = 'Programiranje'

# for slovo in rijec:
#     print(slovo, end=" ")

# koristeci f-string i varijablu rijec
# broj slova u rijeci programiranje je 10

# print(f"Broj slova u rijeci: '{rijec}' je {len(rijec)}.")
# print(f"Broj slova u rijeci: '{rijec}' je {sum(rijec)}.")

# print(ord("A"))

suma = 0
for slovo in rijec:
    suma += ord(slovo)
print(suma)
