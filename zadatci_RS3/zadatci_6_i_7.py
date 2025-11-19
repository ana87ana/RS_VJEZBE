'''6. Kako možete unutar main korutine natjerati event loop da obuhvati ispis unutar korutine
fetch_data(2) bez da ju awaitate unutar main funkcije? Preciznije, dokažite kako se može ispisati
tekst Dovršio sam s 2. unutar korutine fetch_data(2) bez da eksplicitno pozivate await task2
unutar main() funkcije.'''

#Dovrši sam s 2 se ne ispiše zato što se event loop zatvori prije nego što se korutina fetch_data(2)
#izvrši. Dodavajući još jedan await asyncio.sleep() s parametrom koji produžuje event loop dovoljno
#dugo da se korutina izvrši 

import asyncio, time

async def fetch_data(param):
    print(f"Nešto radim s {param}...")
    await asyncio.sleep(param)
    print(f'Dovršio sam s {param}.')
    return f"Rezultat za {param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1)) # schedule
    task2 = asyncio.create_task(fetch_data(2)) #schedule
    result1 = await task1
    print("Fetch 1 uspješno završen.")
    await asyncio.sleep(1) # dodatak
    return [result1]

t1 = time.perf_counter()
results = asyncio.run(main()) # pokretanje event loop-a
t2 = time.perf_counter()
print(results)
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")


'''7. Objasnite korak po korak kako se ponaša event loop (kako se raspoređuju, izvršavaju i dovršavaju
korutine te koja su njihova stanja u različitim fazama izvođenja) na sljedećem primjeru:'''

import asyncio

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]
    await asyncio.gather(*timers)

asyncio.run(main())

'''
1. Pokreće se main korutina i počinje event loop
2. Unutar main korutine se stvaraju tri task zadatka
3. asyncio.gather() prima zadatke
4. Sva tri zadatka se počinju izvršavati 
5. Timeri izmjenično ispisuju koliko je sekundi ostalo u redosljedu Timer 1, Timer 2, Timer 3
5.1. Timer je u aktivnom stanju kad ispisuje preostalo vrijeme, dok su ostali zadatci pauzirani
6. Prvi task završi nakon tri sekunde te nakon toga Timer 2 i Timer 3 izmjenično ispisuju preostalo vrijeme
7. Timer 2 završi te nakon toga Timer 3 završi 
8. Main korutina završi rad te je event loop zatvoren
'''
