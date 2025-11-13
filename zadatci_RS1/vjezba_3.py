a = int(input("Unesite broj od 1 do 100: "))
i = 1

while a != 37:
    if a < 1 and a > 100:
        a = int(input("Broj nije u traženom rasponu. Unesite broj od 1 do 100: "))
    elif a > 37:
        print(f"Broj {a} je veći od traženog broja")
        a = int(input("Unesite broj od 1 do 100: "))
        i+=1
    elif a < 37:
        print(f"Broj {a} je manji od traženog broja")
        a = int(input("Unesite broj od 1 do 100: "))
        i+=1

print(f"Pogođeno u {i} pokušaja") 
    
