def func():
    print(111)
    # yield 1：返回1，并暂停在这里等待下一次调用
    # 调用send: send传入的参数会保存在v1中，下次调用的时候会从这里开始执行
    v1 = yield 1
    print("v1:", v1)

    print(222)
    v2 = yield 2
    print("v2:", v2)

    print(333)
    v3 = yield 3
    print("v3:", v3)

    print(444)


data = func()
# 执行生成器函数，并传给生成器函数参数
# 首次必须先启动生成器函数，data.send(None)或者next(data)
n1 = data.send(None)
print("n1:", n1)

n2 = data.send(666)
print("n2:", n2)

n3 = data.send(777)
print("n3:", n3)

# n4 = data.send(888)
# print(n4)
