class Parent:
    pass


class Parent2:
    pass


class Child(Parent, Parent2):
    pass


# 查看父类
print(Child.__bases__)  # (<class '__main__.Parent'>, <class '__main__.Parent2'>)
print(Child.__mro__)  # 方法解析顺序
