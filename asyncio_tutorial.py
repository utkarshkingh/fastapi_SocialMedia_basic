import asyncio

async def fetch_data(id,sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return{"id": id , "data":f"Sample data from coroutine{id}"}




async def main():
    task1=asyncio.create_task(fetch_data(1,2))
    task2=asyncio.create_task(fetch_data(2,3))
    task3=asyncio.create_task(fetch_data(3,1))

    result1=await task1
    result2=await task2




######### concept 2 #################

import asyncio

async def main():
    task=asyncio.create_task(other_function())
    print("A")
    await asyncio.sleep(2)
    print("B")
    await task


async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("2")


asyncio.run(main())


