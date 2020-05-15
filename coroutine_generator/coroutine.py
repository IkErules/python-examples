from datetime import datetime
import asyncio


class AsyncExample:

    async def await_one_second(self):
        print("hello...")
        await asyncio.sleep(1)
        print("...world, after waiting 1 sec")

    async def await_each_task(self):
        start = self.__get_start_date_time_and_print()
        await self.__wait_and_print(2, 'await_each_task() first call: waited 2 sec')
        await self.__wait_and_print(1, 'await_each_task() second call: waited 1 sec')
        self.__calculate_and_print_duration_from_start_time(start)

    async def run_tasks_parallel(self):
        start = self.__get_start_date_time_and_print()
        # Erstellen von zwei Tasks, welche die Methode __wait_and_print() aufrufen und sogleich ausführen
        task_long = asyncio.create_task(self.__wait_and_print(2, 'run_tasks_parallel() first call: waited 2 sec'))
        task_short = asyncio.create_task(self.__wait_and_print(1, 'run_tasks_parallel() second call: waited 1 sec'))
        await task_long
        await task_short
        self.__calculate_and_print_duration_from_start_time(start)

    async def __wait_and_print(self, seconds_to_wait, to_print):
        await asyncio.sleep(seconds_to_wait)
        print(to_print)

    def __get_start_date_time_and_print(self):
        start = datetime.now()
        print(f"started at {start.strftime('%X')}")
        return start

    def __calculate_and_print_duration_from_start_time(self, start_date_time):
        end_date_time = datetime.now()
        diff = end_date_time - start_date_time
        print(f"finished at {end_date_time.strftime('%X')}")
        print(f"duration {diff} sec")


if __name__ == "__main__":
    async_class = AsyncExample()

    print("------ first example ------")
    asyncio.run(async_class.await_one_second())

    print("------ second example ------")
    asyncio.run(async_class.await_each_task())

    print("------ third example ------")
    asyncio.run(async_class.run_tasks_parallel())
