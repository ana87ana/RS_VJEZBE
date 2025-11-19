import asyncio

lista = [x for x in range(1, 11)]

async def korutina(param):
    await asyncio.sleep(3)
    print("Podatci dohvaćeni")
    return param

async def main():
    return await korutina(lista)
    
asyncio.run(main())