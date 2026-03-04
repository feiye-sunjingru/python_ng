import asyncio
import time


async def task1():
    print("任务1开始执行...")
    # await后面只能跟着async def定义的对象：time.sleep不是
    # 用于暂停当前协程的执行，直到等待的对象（如另一个协程、Task、Future 等）完成
    await asyncio.sleep(5)
    print("任务1执行完毕...")
    return 10


async def task2():
    print("任务2开始执行...")
    await asyncio.sleep(3)  # 模拟一个耗时 3 秒的 I/O 操作
    print("任务2执行完毕...")
    return 20


# 定义一个协程函数：表明交给EventLoop执行


async def main():
    print("开始执行任务...")

    """
    event_loop = asyncio.get_running_loop()
    # task1()是一个协程对象：创建一个Task对象，交给EventLoop调度执行
    t1 = event_loop.create_task(task1())
    t2 = event_loop.create_task(task2())

    result = await t1
    print('任务1执行结果:', result)
    result = await t2
    print('任务2执行结果:', result)
    """

    # 等价上面注释掉的代码：创建Task对象，交给EventLoop调度执行，等待结果
    result = await asyncio.gather(task1(), task2())
    print("任务1执行结果:", result[0])
    print("任务2执行结果:", result[1])


if __name__ == "__main__":
    start = time.time()
    """
    # 创建一个EventLoop
    event_loop = asyncio.get_event_loop()
    # 启动EventLoop，执行main函数：整个任务的执行入口
    event_loop.run_until_complete(main())
    """
    # 跟上面三行等价：创建一个EventLoop，启动EventLoop，执行main函数
    asyncio.run(main())

    print("总耗时:", time.time() - start)
