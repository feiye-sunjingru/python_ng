import builtins

# 查看完整的内置函数列表
print(dir(builtins))

# 注意：列表、字典不能被哈希
# print(hash([1,2]))  # TypeError

"""
Python 36 个常用内置函数示例
按功能分组，便于学习和理解
"""

# ==================== 第 1 组：数值计算函数（5 个）====================
print("=" * 50)
print("第 1 组：数值计算函数")
print("=" * 50)

# abs - 绝对值
v = abs(-10)
print(f"abs(-10) = {v}")  # 10

# pow - 幂运算
v = pow(2, 5)
print(f"pow(2, 5) = {v}")  # 32 (2 的 5 次方)

# sum - 求和
v = sum([-11, 22, 33, 44, 55])
print(f"sum([-11,22,33,44,55]) = {v}")  # 143

# divmod - 同时求商和余数
quotient, remainder = divmod(9, 2)
print(f"divmod(9, 2) = 商{quotient}, 余{remainder}")  # 商 4, 余 1

# round - 四舍五入
v = round(4.11786, 2)
print(f"round(4.11786, 2) = {v}")  # 4.12


# ==================== 第 2 组：最值与逻辑判断（4 个）====================
print("\n" + "=" * 50)
print("第 2 组：最值与逻辑判断")
print("=" * 50)

# min - 最小值（支持多种参数形式）
v1 = min(11, 2, 3, 4, 5)
v2 = min([11, 22, 33, 44, 55])
v3 = min([-11, 2, 33, 44, 55], key=lambda x: abs(x))
print(f"min(11,2,3,4,5) = {v1}")  # 2
print(f"min([11,22,33,44,55]) = {v2}")  # 11
print(f"min(..., key=abs) = {v3}")  # 2 (绝对值最小)

# max - 最大值
v1 = max(11, 2, 3, 4, 5)
v2 = max([11, 22, 33, 44, 55])
print(f"max(11,2,3,4,5) = {v1}")  # 11
print(f"max([11,22,33,44,55]) = {v2}")  # 55

# all - 全部为 True 才返回 True
v = all([11, 22, 44, 0])
print(f"all([11,22,44,0]) = {v}")  # False (0 为假)

# any - 有一个为 True 就返回 True
v = any([11, 22, 44, 0])
print(f"any([11,22,44,0]) = {v}")  # True


# ==================== 第 3 组：进制转换（3 个）====================
print("\n" + "=" * 50)
print("第 3 组：进制转换")
print("=" * 50)

# bin - 十进制转二进制
v = bin(10)
print(f"bin(10) = {v}")  # 0b1010

# oct - 十进制转八进制
v = oct(10)
print(f"oct(10) = {v}")  # 0o12

# hex - 十进制转十六进制
v = hex(10)
print(f"hex(10) = {v}")  # 0xa


# ==================== 第 4 组：字符与编码（2 个）====================
print("\n" + "=" * 50)
print("第 4 组：字符与编码")
print("=" * 50)

# ord - 字符转 Unicode 码点
v = ord("武")
print(f"ord('武') = {v} (十六进制：{hex(v)})")  # 27494

# chr - Unicode 码点转字符
v = chr(27494)
print(f"chr(27494) = {v}")  # 武


# ==================== 第 5 组：类型转换（8 个）====================
print("\n" + "=" * 50)
print("第 5 组：类型转换")
print("=" * 50)

# int - 转整数
x = int("123")
y = int(3.9)
print(f"int('123') = {x}, int(3.9) = {y}")  # 123, 3

# float - 转浮点数
a = float("3.14")
b = float(10)
print(f"float('3.14') = {a}, float(10) = {b}")  # 3.14, 10.0

# bool - 转布尔值
print(f"bool(0) = {bool(0)}, bool(1) = {bool(1)}")  # False, True
print(f"bool('') = {bool('')}, bool('hello') = {bool('hello')}")  # False, True

# str - 字符串编码
s = "武沛齐"
b_utf8 = s.encode("utf-8")
b_gbk = s.encode("gbk")
print(f"'{s}'.encode('utf-8') = {b_utf8}")
print(f"'{s}'.encode('gbk') = {b_gbk}")

# list - 转列表
lst = list("abc")
print(f"list('abc') = {lst}")  # ['a', 'b', 'c']

# dict - 创建字典
d = dict(a=1, b=2)
d2 = dict(zip(["x", "y"], [10, 20]))
print(f"dict(a=1,b=2) = {d}")
print(f'dict(zip(["x", "y"], [10, 20]) = {d2}')

# tuple - 转元组
t = tuple([1, 2, 3])
print(f"tuple([1,2,3]) = {t}")  # (1, 2, 3)

# set - 转集合（去重）
s = set([1, 2, 2, 3])
print(f"set([1,2,2,3]) = {s}")  # {1, 2, 3}


# ==================== 第 6 组：对象与信息（8 个）====================
print("\n" + "=" * 50)
print("第 6 组：对象与信息")
print("=" * 50)

# len - 获取长度
print(f"len([1,2,3,4]) = {len([1,2,3,4])}")  # 4
print(f"len('Hello') = {len('Hello')}")  # 5

# type - 获取类型
print(f"type(10) = {type(10)}")  # <class 'int'>
print(f"type('hello') = {type('hello')}")  # <class 'str'>

# id - 获取内存地址
a = 10
b = a
print(f"id(10) = {id(a)}, id(b) = {id(b)}")  # 相同（同一对象）

# hash - 获取哈希值
h = hash("hello")
print(f"hash('hello') = {h}")

# callable - 判断是否可调用
v1 = "武沛齐"
v2 = lambda x: x


def v3():
    pass


print(f"callable('字符串') = {callable(v1)}")  # False
print(f"callable(lambda) = {callable(v2)}")  # True
print(f"callable(函数) = {callable(v3)}")  # True

# dir - 查看对象属性
print(f"dir(builtins) 返回 {len(dir(builtins))} 个内置名称")

# help - 查看帮助文档
# help(print)  # 取消注释可查看帮助

# print - 打印输出
print(1, 2, 3, sep=" | ")  # 1 | 2 | 3
print("End", end=".\n")  # End.


# ==================== 第 7 组：迭代与序列（6 个）====================
print("\n" + "=" * 50)
print("第 7 组：迭代与序列")
print("=" * 50)

# range - 生成数字序列
print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()

print("range(2, 7, 2):", end=" ")
for i in range(2, 7, 2):
    print(i, end=" ")  # 2 4 6
print()

# enumerate - 带索引遍历
colors = ["red", "green", "blue"]
print("enumerate 遍历:")
for index, color in enumerate(colors):
    print(f"  {index}: {color}")

# zip - 并行遍历多个序列
v1 = [11, 22, 33]
v2 = [55, 66, 77]
v3 = [10, 20, 30]
print("zip 并行遍历:")
for item in zip(v1, v2, v3):
    print(f"  {item}")

# sorted - 排序（返回新列表）
info = {
    "wupeiqi": {"id": 10, "age": 119},
    "root": {"id": 20, "age": 29},
    "seven": {"id": 9, "age": 9},
    "admin": {"id": 11, "age": 139},
}
# 按照key排序
result_key = sorted(info.items())
print("sorted 按 key 排序:")
for name, data in result_key:
    print(f"  {name}: id={data['id']}, age={data['age']}")

# 按 id 排序
result = sorted(info.items(), key=lambda x: x[1]["id"])
print("sorted 按 id 排序:")
for name, data in result:
    print(f"  {name}: id={data['id']}, age={data['age']}")

# 按 age 排序
result_age = sorted(info.items(), key=lambda x: x[1]["age"], reverse=True)
print("sorted 按 age 从大到小排序:")
for name, data in result_age:
    print(f"  {name}: id={data['id']}, age={data['age']}")

data_list = [
    "1-5 编译器和解释器.mp4",
    "1-7 今日作业.mp4",
    "1-9 Python解释器种类.mp4",
    "1-16 今日总结.mp4",
    "1-2 课堂笔记的创建.mp4",
    "1-15 Pycharm使用和破解 (win系统) .mp4",
    "1-12 python解释器的安装 (mac系统) .mp4",
    "1-3 python解释器的安装 (win系统) .mp4",
    "1-8 Python介绍.mp4",
    "1-7 编程语言的分类.mp4",
    "1-3 常见计算机基本概念.mp4",
    "1-14 Pycharm使用和破解 (mac系统) .mp4",
    "1-10 CPython解释器版本.mp4",
    "1-1 今日概要.mp4",
    "1-6 学习编程本质上的三件事.mp4",
    "1-18 作业答案和讲解.mp4",
    "1-4 编程语言.mp4",
    "1-11 环境搭建说明.mp4",
]

result = sorted(data_list, key=lambda x: int(x.split()[0].split("-")[-1]))
print("sorted 按数字排序:")
for item in result:
    print(item)
# ==================== 第 8 组：文件操作（1 个）====================
print("\n" + "=" * 50)
print("第 8 组：文件操作")
print("=" * 50)

if __name__ == "__main__":
    # open - 文件读写
    with open("test.txt", "w", encoding="utf-8") as f:
        f.write("Hello, Python!")

    with open("test.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(f"文件内容：{content}")
