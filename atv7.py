#Simule o download de 10 arquivos, cada um com tempo aleatório, usando asyncio. Exiba a ordem de conclusão.
import asyncio

async def download1():
  print("Iniciando download1")
  await asyncio.sleep(2)
  print("1º Download concluído")
async def download2():
  print("Iniciando download2")
  await asyncio.sleep(3)
  print("2º Download concluido")
async def download3():
  print("Iniciando download3")
  await asyncio.sleep(4)
  print("3º Download concluído")
async def download4():
  print("Iniciando download4")
  await asyncio.sleep(6)
  print("4º Download concluído")
async def download5():
  print("Iniciando download5")
  await asyncio.sleep(8)
  print("5º Download concluído")

async def main():
  await asyncio.gather(
    download1(),
    download2(),
    download3(),
    download4(),
    download5()
  )
asyncio.run(main())