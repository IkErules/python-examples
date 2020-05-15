"""
Übung Java 8, Teil 3+4
---- Nr. 3 ----
"""
import asyncio

HALF_SECOND = 0.5
TWO_SECONDS = 2
THREE_SECONDS = 3
SIX_SECONDS = 6


class AwaitableFuture:

    async def start(self):
        asyncio.create_task(self.__do_async_stuff())
        await self.__print_dots()

    async def __do_async_stuff(self):
        task_1 = asyncio.create_task(self.__wait_and_return_result(THREE_SECONDS))
        task_2 = asyncio.create_task(self.__wait_and_return_result(SIX_SECONDS))
        await task_1
        await task_2
        await self.__do_blocking_wait(TWO_SECONDS)
        waited_time = (task_1.result() + task_2.result() + TWO_SECONDS) * 1000
        self.__print_result("was waiting for %r ms" % waited_time)

    async def __wait_and_return_result(self, time):
        await asyncio.sleep(time)
        self.__print_result(time * 1000)
        return time

    def __print_result(self, result):
        print(str(result))

    async def __do_blocking_wait(self, time):
        await asyncio.sleep(time)

    async def __print_dots(self):
        print("-> Now waiting for things to happen!")
        for i in range(0, 20):
            self.__print_result(".")
            await self.__do_blocking_wait(HALF_SECOND)


awaitable_future = AwaitableFuture()
asyncio.run(awaitable_future.start())
