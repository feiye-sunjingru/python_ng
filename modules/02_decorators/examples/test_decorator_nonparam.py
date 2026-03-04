from functools import wraps


def my_decorator(func):
    # 使用 functools.wraps 装饰内部函数是一个好习惯，用于保留原函数的元信息（如 __name__, __doc__）
    @wraps(func)
    # 虽然名字可以任意，但为了保持代码可读性和一致性，强烈建议使用 wrapper，尤其是在团队协作或开源项目中。
    def wrapper():
        print("Before function call")
        result = func()
        print("After function call")
        return result

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()
# 使用wraps之后，say_hello函数的__name__和__doc__属性被正确地保留了下来，而不是被wrapper函数覆盖掉。
print(say_hello.__name__)
print(say_hello.__doc__)
