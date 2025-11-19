import asyncio

baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
{'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
{'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
{'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
{'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autorizacija(korisnik):
    await asyncio.sleep(2)
    for user in baza_lozinka:
        if user["korisnicko_ime"] == korisnik["korisnicko_ime"]:
            check = user["lozinka"]
            
    if check == korisnik["lozinka"]:
        return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija uspješna."
    else:
        return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija neuspješna."


async def autentifikacija(korisnik):
    await asyncio.sleep(3)
    postojeci_user = any(korisnik["korisnicko_ime"] == trazeni_user["korisnicko_ime"] and korisnik["email"] == trazeni_user["email"] for trazeni_user in baza_korisnika)
    if postojeci_user:
        return await autorizacija(korisnik)
    else:
        return f"Korisnik {korisnik} nije pronađen."
    
async def main():
    provjera = await autentifikacija({'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com', 'lozinka': 'lozinka123'})
    print(provjera)
    
asyncio.run(main())