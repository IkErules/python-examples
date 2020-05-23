"""
Übung Java 8, Teil 3+4
---- Nr. 3 ----

expected output:
-> Now waiting for things to happen!
......3000......6000.....was waiting for 11000ms...
"""
import asyncio

HALF_SECOND = 0.5
TWO_SECONDS = 2
THREE_SECONDS = 3
SIX_SECONDS = 6


class AwaitableFuture:

    async def start(self):
        asyncio.create_task(self.__do_async_stuff_with_futures())
        await self.__print_dots()

    async def __do_async_stuff_with_futures(self):
        # Get the current event loops and creates futures
        loop = asyncio.get_running_loop()
        future_1 = loop.create_future()
        future_2 = loop.create_future()

        # Creates two parallel tasks and passes futures as params
        asyncio.create_task(self.__wait_and_set_result_in_future(THREE_SECONDS, future_1))
        asyncio.create_task(self.__wait_and_set_result_in_future(SIX_SECONDS, future_2))

        # Futures are awaitable and result can be assigned to a variable
        result_future_1 = await future_1
        result_future_2 = await future_2

        await self.__do_blocking_wait(TWO_SECONDS)
        waited_time = (result_future_1 + result_future_2 + TWO_SECONDS) * 1000
        self.__print_result("was waiting for %r ms" % waited_time)

    async def __wait_and_set_result_in_future(self, time, future):
        await asyncio.sleep(time)
        self.__print_result(time * 1000)
        future.set_result(time)

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
