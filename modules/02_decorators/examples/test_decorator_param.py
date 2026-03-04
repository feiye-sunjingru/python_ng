from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling function with args:", args, kwargs)
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def add(a, b):
    return a + b


print(add(3, 5))
print(add.__name__)
print(add.__doc__)
