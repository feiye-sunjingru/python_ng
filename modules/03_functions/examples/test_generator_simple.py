def func():
    print(123)
    yield 1234  # 有点像return，执行到这个位置之后，就不再执行。
    print(456)
    yield 666
    print(789)


# 执行生成器函数时，函数体默认不会被执行；返回的是一个生成器对象。
v1 = func()
print(v1)  # <generator object func at 0x7fd0280f75f0>

"""
# next里面放生成器对象，进入生成器函数并执行其中的代码
n1 = next(v1)
print(n1)  # 1234

n2 = next(v1)
print(n2)  # 666

n3 = next(v1)
print(n3)  # StopIteration异常，说明生成器已经没有值可以产出了
"""

# 基于生成器对象创建一个迭代器，可以使用for循环来迭代生成器产出的值
for i in v1:
    print(i)
