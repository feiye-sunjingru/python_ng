import asyncio


async def task():
    print("task")


async def demo():
    # 协程函数，执行结果需要通过await获取
    coro = await task()
    # task()是一个协程对象，必须通过await获取结果
    print(type(task()))
    print(type(coro))


if __name__ == "__main__":
    # 协程对象必须通过event_loop才能执行
    asyncio.run(demo())
