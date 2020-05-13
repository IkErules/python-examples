"""
Übung Java 9, Teil 3+4
---- Nr. 3 ----
"""
import asyncio

HALF_SECOND = 0.5
TWO_SECONDS = 2
THREE_SECONDS = 3
SIX_SECONDS = 6


async def start():
    asyncio.create_task(do_async_stuff())
    await print_dots()


async def do_async_stuff():
    task_1 = asyncio.create_task(wait_and_return_result(THREE_SECONDS))
    task_2 = asyncio.create_task(wait_and_return_result(SIX_SECONDS))

    await task_1
    await task_2

    await do_blocking_wait(TWO_SECONDS)
    waited_time = (task_1.result() + task_2.result() + TWO_SECONDS) * 1000
    print_result("was waiting for %r ms" % waited_time)


async def wait_and_return_result(time):
    await asyncio.sleep(time)
    print_result(time * 1000)
    return time


def print_result(result):
    print(str(result))


async def print_dots():
    print("-> Now waiting for things to happen!")
    for i in range(0, 20):
        print_result(".")
        await do_blocking_wait(HALF_SECOND)


async def do_blocking_wait(time):
    await asyncio.sleep(time)


asyncio.run(start())
