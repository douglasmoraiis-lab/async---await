#treinando nova forma de criar tarfas utilizando em conjunto random

import asyncio
import random

async def tarefa(nome):
  print(f"Iniciando {nome}")
  tempo = random.uniform(1, 5)
  await asyncio.sleep(tempo)
  return f"{nome} finalizada em {tempo:.2f}s"
async def main():
  tarefas = [tarefa(f"Tarefa {i}") for i in range(1, 6)]

  for concluida in asyncio.as_completed(tarefas):
    resultado = await concluida
    print(resultado)
asyncio.run(main())
