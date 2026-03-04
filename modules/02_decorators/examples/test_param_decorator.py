from functools import wraps

"""
装饰器也能接收参数，这就需要三层嵌套
"""


def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def greet():
    print("Hi!")


greet()
