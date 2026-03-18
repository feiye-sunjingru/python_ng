import threading


# 线程安全的单例（使用锁）
class Singleton:
    _instance = None
    _lock = threading.Lock()

    # 它在对象创建过程中被自动调用，早于 __init__
    # 虽然 __new__ 的第一个参数是 cls（代表类本身），
    # 但它 并不是一个普通的类方法（class method），而是一个 由 Python 解释器特殊处理的方法。
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                # 双重检查锁定（Double-checked locking）
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance


singleton = Singleton()
singleton2 = Singleton()
print(singleton is singleton2)
