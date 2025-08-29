import asyncio

async def minha_funcao():
  print("Olá ...")
  await asyncio.sleep(2)
  print("Mundo!")
asyncio.run(minha_funcao())








