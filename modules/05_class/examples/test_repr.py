class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 给开发者使用
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # 给用户使用
    def __str__(self):
        return f"({self.x}, {self.y})"


p = Point(1, 2)
# 优先使用__str__:如果没有定义__str__，则使用__repr__
print(p)
print(repr(p))  # 输出: Point(1, 2)

print(repr(42))
print(repr("hello"))
print(repr([1, 2, 3]))

# eval 用于执行字符串形式的代码，存在严重的安全风险（如代码注入）
print(eval(repr(42)))
print(eval(repr("hello")))
print(eval(repr([1, 2, 3])))
