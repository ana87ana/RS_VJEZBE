a = int(input("Unesite godinu: "))

if (a%4 == 0 and a%100 != 0) or a%400 == 0:
    print(f"Godina {a}. je prijestupna")
else:
    print(f"Godina {a}. nije prijestupna")