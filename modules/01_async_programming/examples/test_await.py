import asyncio


async def sub_task():
    print('sub_task')
    return 100

async def sub_task2():
    print('sub_task2')
    return 200

async def task01():
    print('task01')
    # 一般情况下，await+协程对象：EventLoop不会直接切换到其他任务执行
    # 因此不是task01->task02...
    result = await sub_task()
    return result

async def task02():
    print('task02')
    # 而asyncio.sleep内部会执行await future对象，所以会切换到其他任务执行: task02->task03->sub_task2...
    await asyncio.sleep(1)  # 模拟一个耗时 1 秒的 I/O 操作
    result = await sub_task2()
    return result

async def task03():
    print('task03')
    return 300

async def start():
    # 在事件循环中注册两个任务 task01 和 task02
    # 并等待两个任务的执行结果

    # <class 'asyncio.tasks._GatheringFuture'>
    # print(type(asyncio.gather(task01(), task02())))

    result = await asyncio.gather(task01(), task02(), task03())
    print(result)
    

if __name__ == '__main__':
    asyncio.run(start())