def greet():
    return "Hello!"


def call_func(func):
    return func()


print(call_func(greet))  # 输出: Hello!
