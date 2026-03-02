import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def thread_task(future):
    time.sleep(5)  # 模拟耗时的 I/O 操作
    future.set_result(100)  # 设置 future 的结果

async def sub_task():
    print('sub task 开始')

    # 获取当前事件循环
    event_loop = asyncio.get_running_loop()
    
    # 创建 future 对象
    future = event_loop.create_future()

    # 创建线程池执行器
    executor = ThreadPoolExecutor()

    # 在其他线程中执行任务（非阻塞）
    event_loop.run_in_executor(executor, thread_task, future)

    # 挂起当前任务，等待 future 返回结果
    result = await future

    print('sub task 结束')
    return result

async def task1():
    print('task1 开始')
    result = await sub_task()
    print('task1 结束')
    return result

async def task2():
    print('task2 开始')
    await asyncio.sleep(1)  # 模拟其他任务的执行
    print('task2 结束')
    return 200

async def main():
    # 并发执行 task1 和 task2
    result = await asyncio.gather(task1(), task2())
    print(result)

if __name__ == '__main__':
    asyncio.run(main())