"""
用类实现装饰器
"""


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)


# say_hi = CountCalls(say_hi)，需要实现函数的 __call__ 方法
@CountCalls
def say_hi():
    print("Hi!")


say_hi()  # 1 times
say_hi()  # 2 times
