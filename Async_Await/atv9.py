#Crie uma função que demora 5 segundos para terminar. Use asyncio.wait_for() para cancelar a execução se ela demorar mais de 2 segundos.i
import asyncio 

async def funcao_pausa():
  print("Started funcao_pausa")
  await asyncio.sleep(5)
  print("Funcao_pausa finished")

async def main():
  try:
    result = await asyncio.wait_for(funcao_pausa(), timeout=2)
    print(f"Received result: {result}")
  except asyncio.TimeoutError:
    print("Task timed out!")

if __name__ == "__main__":
    asyncio.run(main())