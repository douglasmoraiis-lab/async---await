import asyncio

async def funcao_1():
  print("Iniciando funcao_1")
  await asyncio.sleep(2)
  print("funcao_1 concluida")

async def funcao_2():
    print("Iniciando funcao_2")
    await asyncio.sleep(5)
    print("funcao_2 concluida")

async def main():
  await asyncio.gather(
    funcao_1(), 
    funcao_2()
  )
asyncio.run(main())