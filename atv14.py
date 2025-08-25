#Baixe 20 “arquivos”, mas só permita 3 downloads simultâneos usando um semáforo (asyncio.Semaphore).
import asyncio
import random 

async def baixar_arquivo(nome):
  print(f"Iniciando download do {nome}")
  await asyncio.sleep(random.uniform(1, 5))
  print(f"Download do {nome} concluido")
  return nome

async def main():
  tarefas = [
    baixar_arquivo(f"Arquivo{i}") for i in range(1, 21)
  ]
  resultados = await asyncio.gather(*tarefas)
  print("\n Todos os downloads concluídos", resultados)

asyncio.run(main())