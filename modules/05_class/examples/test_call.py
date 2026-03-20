print("=" * 60)
print("__call__ 方法 - 让实例对象可调用")
print("=" * 60)
print("\n【核心概念】定义 __call__ 后，实例可以像函数一样被调用\n")


class Greeter:
    """最简单的 __call__ 示例"""

    def __init__(self, name: str) -> None:
        self.name = name

    def __call__(self) -> None:
        print(f"Hello, {self.name}!")


greet_alice = Greeter("Alice")
greet_bob = Greeter("Bob")

print(f"callable(greet_alice): {callable(greet_alice)}")  # True
print(f"callable(42): {callable(42)}")  # False

greet_alice()  # Hello, Alice!
greet_bob()  # Hello, Bob!

print("\n" + "=" * 60)
print("场景 1：接收任意参数的 __call__")
print("=" * 60)


class Logger:
    """模拟日志记录器，接收任意参数"""

    def __call__(self, *args, **kwargs) -> None:
        print(f"Logged: args={args}, kwargs={kwargs}")


log = Logger()
log(1, 2, 3)
log("error", code=500, message="Something wrong")

print("\n" + "=" * 60)
print("场景 2：使用 __call__ 实现装饰器")
print("=" * 60)


class Memoize:
    """使用 __call__ 实现记忆化装饰器"""

    def __init__(self, func) -> None:
        self.func = func
        self.cache: dict[tuple, int] = {}

    def __call__(self, *args) -> int:
        """缓存已计算的结果，避免重复计算"""
        if args not in self.cache:
            # 记录参数和结果
            self.cache[args] = self.func(*args)
        return self.cache[args]


@Memoize
def fib(n: int) -> int:
    """计算斐波那契数列（带缓存）"""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(f"fib(10) = {fib(10)}")
print(f"fib(20) = {fib(20)}")
print(f"fib(30) = {fib(30)}")

print("\n" + "=" * 60)
print("场景 3：带状态的 callable 对象")
print("=" * 60)


class Counter:
    """带状态的计数器，每次调用递增"""

    def __init__(self, start: int = 0) -> None:
        self.count = start

    def __call__(self) -> int:
        self.count += 1
        return self.count

    def reset(self) -> None:
        self.count = 0


counter = Counter(100)
print(f"初始值：{counter()}")  # 101
print(f"第二次：{counter()}")  # 102
print(f"第三次：{counter()}")  # 103
counter.reset()
print(f"重置后：{counter()}")  # 1

print("\n" + "=" * 60)
print("场景 4：__call__ 与闭包对比")
print("=" * 60)


def make_multiplier_class(n: int):
    """使用类实现的乘法器"""

    class Multiplier:
        def __init__(self, factor: int) -> None:
            self.factor = factor

        def __call__(self, x: int) -> int:
            return x * self.factor

    return Multiplier(n)


def make_multiplier_func(n: int):
    """使用闭包实现的乘法器"""

    def multiplier(x: int) -> int:
        return x * n

    return multiplier


double_class = make_multiplier_class(2)
double_func = make_multiplier_func(2)

print(f"类方式：double_class(5) = {double_class(5)}")
print(f"闭包方式：double_func(5) = {double_func(5)}")

print("\n" + "=" * 60)
print("总结")
print("=" * 60)
print("""
__call__ 方法的核心价值：

1. 让实例可调用：instance() 等价于 instance.__call__()
2. 保持状态：可以在多次调用间维护内部状态
3. 实现装饰器：类装饰器需要 __call__ 方法
4. 替代闭包：提供面向对象的方式实现类似功能

适用场景：
- 需要保持状态的 callable 对象
- 类装饰器的实现
- 策略模式中的可调用策略
- 回调函数的面向对象实现
""")
