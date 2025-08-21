import asyncio 
async def long_running_task():
  print("Task started")
  await asyncio.sleep(5) #simulate a task taking 5 seconds
  print("Task finished")
  return "Task rsult"

async def main():
  try:
    result = await asyncio.wait_for(long_running_task(), timeout=2)
    print(f"Received result: {result}")
  except asyncio.TimeoutError:
    print("Task time out!")

if __name__ == "__main__":
  asyncio.run(main())