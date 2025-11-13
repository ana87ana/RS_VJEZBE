cijeli_broj = int(input("Unesite broj: "))
rezultat = 0

while cijeli_broj != 0:
    rezultat += cijeli_broj
    cijeli_broj = int(input("Unesite broj: "))

print(f"Zbroj svij brojeva kojih ste unijeli je: {rezultat}")