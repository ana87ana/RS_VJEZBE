lozinka = input("Unesite lozinku: ")

def provjeraLozinke(lozinka):
    if len(lozinka) < 8 or len(lozinka) > 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova")
    elif "password" in lozinka or "lozinka" in lozinka:
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
        
provjeraLozinke(lozinka)

