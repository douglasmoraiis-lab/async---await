import asyncio 


async def teste():
  print("Iniciando teste 1")
  await asyncio.sleep(3)
  return("Teste 1 concluido")

async def teste2():
  print("Iniciando teste 2")
  await asyncio.sleep(4)
  return("Teste 2 concluido")

async def main():
  await asyncio.gather(
    teste(),
    teste2()
  )
asyncio.run(main())