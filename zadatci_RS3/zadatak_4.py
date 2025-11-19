import asyncio
import random

async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    if broj%2 == 0:
        return f"Broj {broj} je paran."
    else:
        return f"Broj {broj} je neparan."

async def main():
    lista = [x for x in random.sample(range(1, 101), 10)]
    zadataci = [asyncio.create_task(provjeri_parnost(x)) for x in lista]
    print(await asyncio.gather(*zadataci))

asyncio.run(main())