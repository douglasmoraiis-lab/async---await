import asyncio 

async def download_image():
 print("iniciando o download_image")
 await asyncio.sleep(4)
 print("Download_image concluído")

async def download_video():
 print("Iniciando o download_video")
 await asyncio.sleep(6)
 print("Download_video concluído")

async def download_audio():
 print("Iniciando o download_audio")
 await asyncio.sleep(8)
 print("Download_audio concluído")

async def main():
 task1 = asyncio.create_task(download_image())
 task2 = asyncio.create_task(download_video())
 task3 = asyncio.create_task(download_audio())

 await asyncio.gather(
 task1,
 task2,
 task3
)
asyncio.run(main())