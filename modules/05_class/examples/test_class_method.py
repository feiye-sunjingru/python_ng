# test_class_method.py
# 类方法 (@classmethod) 使用示例


class Person:
    """演示类方法作为替代构造函数"""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, person_str: str) -> "Person":
        """从字符串解析创建 Person 实例"""
        name, age = person_str.split("-")
        return cls(name, int(age))  # cls 指向实际调用的类


# 使用示例
p1 = Person("Alice", 30)
p2 = Person.from_string("Bob-25")
print(p2.name, p2.age)  # 输出: Bob 25


class Counter:
    """演示类方法访问类变量"""

    count = 0  # 类变量

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls) -> int:
        """获取当前实例计数"""
        return cls.count


# 使用示例
c1 = Counter()
c2 = Counter()
print(Counter.get_count())  # 输出: 2


class Animal:
    """演示类方法在继承中的行为"""

    species = "Unknown"

    @classmethod
    def info(cls) -> str:
        """返回物种信息"""
        return f"This is a {cls.species}"


class Dog(Animal):
    species = "Dog"


# 继承场景验证
print(Dog.info())  # 输出: This is a Dog (cls 绑定到 Dog 类)
