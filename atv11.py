#Criar várias tarefas que terminam em tempos diferentes e exibir os resultados na ordem de conclusão
import asyncio
import random

async def tarefa(n):
    delay = random.uniform(1, 4)
    print(f"Tarefa {n} iniciada, demora {delay:.2f}s...")
    await asyncio.sleep(delay)
    return f"Tarefa {n} concluída em {delay:.2f}s."

async def main():
    tarefas = [tarefa(i) for i in range(5)]

    print("\n--- Executando com for ")
    for concluida in asyncio.as_completed(tarefas):
        resultado = await concluida
        print(resultado)

asyncio.run(main())
