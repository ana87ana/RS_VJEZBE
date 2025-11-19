import asyncio

async def secure_data(rjecnik):
    await asyncio.sleep(3)
    return dict(prezime=rjecnik["prezime"], broj_kartice=hash(rjecnik["broj_kartice"]), CVV=hash(rjecnik["CVV"]))

async def main():
    rjecnik = [{"prezime": "maric", "broj_kartice": "1234567809091423", "CVV": "010"},
               {"prezime": "horvat", "broj_kartice": "1234564444091423", "CVV": "777"},
               {"prezime": "kovac", "broj_kartice": "7734567999095555", "CVV": "123"}]
    zadataci = [asyncio.create_task(secure_data(x)) for x in rjecnik]
    print(await asyncio.gather(*zadataci))

asyncio.run(main())