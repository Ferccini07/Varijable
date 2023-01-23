brojevi = []
for broj in range(0, 21):
    brojevi.append(broj)

brojevi.append(15)

print(brojevi)

print()

# brojevi.clear()

# print(brojevi)

brojevi_kopija = brojevi.copy()

brojevi_count = brojevi.count(15)
print("Broj pojaviljivanja broja 15 u listi je: ", brojevi_count)

# rijeci = ["Python", "algebra", "programiranje"]
# brojevi.extend(rijeci)

print(brojevi)

index_elementa_12 = brojevi.index(12)
print(index_elementa_12)

# brojevi.insert(1, "kesa")
# print(brojevi)

brojevi.sort()
print(brojevi)

brojevi.reverse()
print(brojevi)
