import asyncio 

async def tarefa(nome, duracao):
  print("Iniciando tarefa..")
  await asyncio.sleep(duracao)
  print("Tarefa concluída.")
async def main():
  await asyncio.gather(
    tarefa("A", 4),
    tarefa("B", 5),
    tarefa("C", 6)
  )
asyncio.run(main())