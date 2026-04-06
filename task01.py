text = input("Toliq yozing, ism, familya, vhk; ")


parts = text.split()

natija = " ".join(parts[1:]) + ", " + parts[0]

print(natija)