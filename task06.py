
gap = input("Gap kiriting: ")
sozlar = gap.split()

palindromlar = []
for soz in sozlar:
    if soz.lower() == soz.lower()[::-1]:
        palindromlar.append(soz)

print(palindromlar)