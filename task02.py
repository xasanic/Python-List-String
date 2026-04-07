
sohalar = input("Sohalarni kiriting: ")
result = sohalar.lower().replace(" ", "_").replace(",", "").replace("__", "_")
print(result)