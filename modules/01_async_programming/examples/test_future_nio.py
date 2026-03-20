import asyncio


def cpu_bound_task(n):
    # 模拟耗时计算（无任何 IO）
    total = sum(i * i for i in range(n))
    return total


async def main():
    loop = asyncio.get_running_loop()
    # 将同步函数提交到线程池，返回一个 Future-like 对象（asyncio.Future）
    # 通过 run_in_executor，将耗时计算放到线程池中执行，主线程可以继续处理其他异步任务。
    future = loop.run_in_executor(None, cpu_bound_task, 10_000_000)
    result = await future  # 非 IO 操作，但用了 Future
    print(result)


asyncio.run(main())
