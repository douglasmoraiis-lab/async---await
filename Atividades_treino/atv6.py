#Crie duas funções assíncronas que exibem mensagens com tempos de espera diferentes e execute-as em paralelo. Observe a ordem de execução.
import asyncio

async def tarefa1():
  print("Iniciando tarefa1")
  await asyncio.sleep(2)
  print("Tarefa1 executada com sucesso")

async def tarefa2():
  print("Iniciando tarefa2")
  await asyncio.sleep(4)
  print("Tarefa2 executada com sucesso")

async def main():
  await asyncio.gather(
    tarefa1(), 
    tarefa2()
  )
asyncio.run(main())