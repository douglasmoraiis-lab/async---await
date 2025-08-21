
import asyncio
import random

async def download_file(file_name, delay):
  print(f"Inicando o download '{file_name}'...")
  await asyncio.sleep(delay)
  return f"'{file_name}' terminou o download em {delay:.2f}s."

async def main():
    task = [
        download_file("Imagem_1.jpg", random.uniform(1, 5)),
        download_file("video.mp4", random.uniform(1, 5)),
        download_file("relatorio.pdf", random.uniform(1,5)),
        download_file("documento.txt", random.uniform(1,5)),
        download_file("Musica.mp3", random.uniform(1,5))
    ]
    print("Iniciando todos os downloads..")

    for completed_task in asyncio.as_completed(task):
      result = await completed_task
      print("Tarefa Concluída: {result}")
if __name__ == "__main__":
    asyncio.run(main())

















    