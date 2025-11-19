import asyncio
import time

baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

proizvodi = [
    {"naziv": "mlijeko", "cijena" : "0.92"},
    {"naziv": "kruh", "cijena": "1.54"}
]

async def dohvati_korisnike(rjecnik):
    await asyncio.sleep(3)
    return print(rjecnik)

async def dohvati_proizvode(rjecnik):
    await asyncio.sleep(5)
    return print(rjecnik)
    

async def main():
    await asyncio.gather(dohvati_korisnike(baza_korisnika), dohvati_proizvode(proizvodi))
    
t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()

print(round(t2-t1,2))