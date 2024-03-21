import asyncio


#First task
async def first_task():
      print("Iniciando tarea 1")
      await asyncio.sleep(1)
      print("Terminando tarea 1...")

#Second task
async def second_task():
      print("Iniciando tarea 2")
      await asyncio.sleep(4)
      print("Terminando tarea 2...")


async def main():
      first = asyncio.create_task(first_task())
      second = asyncio.create_task(second_task())
      await asyncio.gather(first_task(), second_task())

asyncio.run(main())

