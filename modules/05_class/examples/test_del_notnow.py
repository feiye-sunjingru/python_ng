class Node:
    def __init__(self, name):
        self.name = name
        self.ref = None
        print(f"{self.name} 被创建")

    def __del__(self):
        print(f"{self.name} 被销毁")


# 创建两个互相引用的对象
a = Node("A")  # a引用计数=1
b = Node("B")  # b引用计数=1
a.ref = b  # a引用计数=2
b.ref = a  # b引用计数=2

# 删除外部引用
del a  # a引用计数=2-1=1
del b  # b引用计数=2-1=1

# 循环引用 + __del__ 导致无法回收: 在运行完成之后才触发del操作
print("End of script")
