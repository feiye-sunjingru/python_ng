import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result

    return wrapper


@timer
def slow_function():
    time.sleep(1)


slow_function()  # 输出: slow_function took 1.0012 secondsslow_function()  # 输出: slow_function took 1.0012 seconds
