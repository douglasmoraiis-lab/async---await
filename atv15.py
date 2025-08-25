#Implemente um produtor que gera itens e múltiplos consumidores que processam esses itens em paralelo usando asyncio.Queue.

import asyncio
import random

async def produtor(queue: asyncio.Queue, total_itens: int):
  for i in range(1, total_itens +1):
    await  asyncio.sleep(random.uniform(0.1, 0.5)) 
    item = f"item_{i}"
    await queue.put(item)
    print(f"[Produtor] Gerou: {item}")

  for _ in range(NUM_CONSUMIDORES):
    await queue.put(None)

async def consumidor(nome: str, queue: asyncio.Queue):
  while True:
    item = await queue.get()
    if item is None:
      print(f"[{nome}] Recebeu sinal para parar.")
      queue.task_done()
      break

    print(f"[{nome}] Processando {item}...")
    await asyncio.sleep(random.uniform(0.5, 1.5))
    print(f"[{nome}]Concluiu {item}")
    queue.task_done()
async def main():
    queue = asyncio.Queue()
    total_itens = 15
    global NUM_CONSUMIDORES
    NUM_CONSUMIDORES = 3
    produtor_task = asyncio.create_task(produtor(queue, total_itens))

    # Cria múltiplos consumidores
    consumidores_tasks = [
        asyncio.create_task(consumidor(f"Consumidor-{i+1}", queue))
        for i in range(NUM_CONSUMIDORES)
    ]

    # Aguarda todas as tarefas terminarem
    await asyncio.gather(produtor_task)
    await queue.join()  # Espera até que todos os itens sejam processados
    await asyncio.gather(*consumidores_tasks)

asyncio.run(main())