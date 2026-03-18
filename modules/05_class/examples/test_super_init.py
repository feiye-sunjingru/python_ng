# 在 Python 3 中，通常直接使用 super()（不带参数），Python 会自动推断当前类和实例。
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal created: {self.name}")


class Dog(Animal):
    def __init__(self, name, breed):
        # super()调用MRO链的下一个类
        super().__init__(name)  # 调用父类的 __init__
        self.breed = breed
        print(f"Dog created: {self.breed}")


d = Dog("Buddy", "Golden Retriever")
