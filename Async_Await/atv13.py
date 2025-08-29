#Criar várias tarefas assíncronas, executar com gather() e depois com as_completed() para ver a diferença no comportamento da ordem dosresultados
import asyncio
import random
import time

async def tarefa(n):
    delay = random.uniform(1, 4)
    print(f"Tarefa {n} iniciada, demora {delay:.2f}s...")
    await asyncio.sleep(delay)
    return f"Tarefa {n} concluída em {delay:.2f}s."

async def main():
    tarefas = [tarefa(i) for i in range(5)]

    print("\n--- Usando gather (ordem fixa) ---")
    inicio = time.perf_counter()
    resultados = await asyncio.gather(*tarefas)
    for r in resultados:
        print(r)
    print(f"Tempo total: {time.perf_counter() - inicio:.2f}s")

    print("\n--- Usando as_completed (ordem de conclusão) ---")
    tarefas = [tarefa(i) for i in range(5)]  # recriar as tarefas
    inicio = time.perf_counter()
    for concluida in asyncio.as_completed(tarefas):
        resultado = await concluida
        print(resultado)
    print(f"Tempo total: {time.perf_counter() - inicio:.2f}s")

asyncio.run(main())
