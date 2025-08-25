import asyncio
import random

async def produtor(queue: asyncio.Queue, total_itens: int):
    for i in range(1, total_itens + 1):
        await asyncio.sleep(random.uniform(0.1, 0.5))  
        item = f"item_{i}"
        await queue.put(item)
        print(f"Produtor produziu: {item}")
    await queue.put(None)  

async def consumidor(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if item is None:  
            break
        await asyncio.sleep(random.uniform(0.2, 0.6))  
        print(f"Consumidor processou: {item}")

async def main():
    fila = asyncio.Queue()
    total_itens = 5

    await asyncio.gather(
        produtor(fila, total_itens),
        consumidor(fila)
    )

asyncio.run(main())