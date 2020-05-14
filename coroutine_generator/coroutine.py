import asyncio
import time


# TODO: Als Klasse implementieren, mit schöneren Methoden aufruf.

async def await_example():
    print("hello...")
    await asyncio.sleep(1)
    print("...world")


print("------ first example ------")
asyncio.run(await_example())


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def await_time_example():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


print("------ second example ------")
asyncio.run(await_time_example())


async def nested():
    print(42)


async def task_example():
    # Erstellen eines Tasks, welche die Methode nested() erstellt und ausführt
    task = asyncio.create_task(nested())

    # Task kann awaited werden oder nebenläufig ausgeführt werden
    await task


print("------ third example ------")
asyncio.run(task_example())
