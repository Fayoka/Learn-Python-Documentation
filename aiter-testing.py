import asyncio

# Definieer een asynchrone generator
async def async_gen():
    for i in range(5):
        await asyncio.sleep(1)  # Simuleer een I/O-operatie
        yield i

async def main():
    async_iterator = aiter(async_gen())  # Krijg de asynchrone iterator
    async for value in async_iterator:     # Asynchroon itereren over de waarden
        print(value)

# Voer de hoofd coroutine uit
asyncio.run(main())
