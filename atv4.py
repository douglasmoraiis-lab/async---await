import asyncio
import random

async def buscar_dados(api):
    print("Iniciando a busca de dados")
    tempo_random = random.randint(1, 3)
    await asyncio.sleep(tempo_random)
    return f"Dados da API {api} obtidos com sucesso"
  
async def main():
    resultado = await buscar_dados("API_1")
    print("Resultado:", resultado)
    
asyncio.run(main())