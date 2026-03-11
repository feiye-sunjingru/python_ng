"""
Python 模块测试示例
包含：字符串处理、字典操作、推导式、闭包陷阱、生成器
"""

# ==================== 第 1 组：字符串处理 ====================
print("=" * 50)
print("第 1 组：字符串处理")
print("=" * 50)

data_list = [
    "1-5 编译器和解释器.mp4",
    "1-7 今日作业.mp4",
    "1-9 Python 解释器种类.mp4",
    "1-16 今日总结.mp4",
    "1-2 课堂笔记的创建.mp4",
    "1-15 Pycharm 使用和破解 (win 系统) .mp4",
    "1-12 python 解释器的安装 (mac 系统) .mp4",
    "1-3 python 解释器的安装 (win 系统) .mp4",
    "1-8 Python 介绍.mp4",
    "1-7 编程语言的分类.mp4",
    "1-3 常见计算机基本概念.mp4",
    "1-14 Pycharm 使用和破解 (mac 系统) .mp4",
    "1-10 CPython 解释器版本.mp4",
    "1-1 今日概要.mp4",
    "1-6 学习编程本质上的三件事.mp4",
    "1-18 作业答案和讲解.mp4",
    "1-4 编程语言.mp4",
    "1-11 环境搭建说明.mp4",
]

# 方法 1：使用 rsplit 去除后缀
result1 = [i.rsplit(".", 1)[0] for i in data_list]
print(f"方法 1 (rsplit)：{result1[:3]}...")  # 只显示前 3 个

# 方法 2：使用 endswith + rstrip 去除后缀
result2 = [i if not i.endswith(".mp4") else i.rstrip(".mp4") for i in data_list]
print(f"方法 2 (rstrip)：{result2[:3]}...")


# ==================== 第 2 组：字典操作 ====================
print("\n" + "=" * 50)
print("第 2 组：字典操作")
print("=" * 50)

# 2.1 字典键值对拼接
info = {"name": "武沛齐", "email": "xxx@live.com", "gender": "男"}
result = ";".join([f"{k}-{v}" for k, v in info.items()])
print(f"字典拼接：{result}")

# 2.2 字典按键排序
info2 = {
    "sign_type": "MD5",
    "out_refund_no": "12323",
    "appid": "wx55cca0b94f723dc7",
    "mch_id": "1526049051",
    "out_trade_no": "ffff",
    "nonce_str": "sdfdfdf",
    "total_fee": 9901,
    "refund_fee": 10000,
}

# 方法 1：字典推导式排序
sorted_info2 = {k: v for k, v in sorted(info2.items(), key=lambda x: x[0])}
print(f"排序后字典：{sorted_info2}")

# 方法 2：排序后拼接成字符串（常用于 API 签名）
sorted_items = sorted(info2.items())
result = "&".join([f"{k}={v}" for k, v in sorted_items])
print(f"API 签名字符串：{result}")


# ==================== 第 3 组：列表推导式与闭包陷阱 ====================
print("\n" + "=" * 50)
print("第 3 组：列表推导式与闭包陷阱")
print("=" * 50)

# 3.1 闭包陷阱示例（错误写法）
print("【错误写法】所有 lambda 共享同一个 i")
data_list = [lambda x: x + i for i in range(10)]
v1 = data_list[0](100)
v2 = data_list[3](100)
print(f"data_list[0](100) = {v1}")  # 109 (i=9)
print(f"data_list[3](100) = {v2}")  # 109 (i=9)
print("原因：循环结束时 i=9，所有 lambda 都引用同一个 i")

# 3.2 正确写法（使用默认参数捕获当前值）
print("\n【正确写法】使用默认参数捕获当前 i 值")
data_list2 = [lambda x, i=i: x + i for i in range(10)]
v1 = data_list2[0](100)
v2 = data_list2[3](100)
print(f"data_list2[0](100) = {v1}")  # 100 (i=0)
print(f"data_list2[3](100) = {v2}")  # 103 (i=3)
print("原因：默认参数在定义时求值，捕获了当时的 i 值")


# ==================== 第 4 组：生成器与闭包 ====================
print("\n" + "=" * 50)
print("第 4 组：生成器与闭包")
print("=" * 50)

# 4.1 列表返回生成器（闭包陷阱）
print("【列表返回】所有函数共享同一个 i")


def num_list():
    return [lambda x: i * x for i in range(4)]


result = [m(2) for m in num_list()]
print(f"结果：{result}")  # [6, 6, 6, 6] (i 最终为 3)

# 4.2 生成器返回（同样有闭包陷阱）
print("\n【生成器返回】同样共享同一个 i")


def num_generator():
    return (lambda x: i * x for i in range(4))


result = [m(2) for m in num_generator()]
print(f"结果：{result}")  # [6, 6, 6, 6] (i 最终为 3)

# 4.3 正确写法
print("\n【正确写法】使用默认参数捕获 i")


def num_correct():
    return [lambda x, i=i: i * x for i in range(4)]


result = [m(2) for m in num_correct()]
print(f"结果：{result}")  # [0, 2, 4, 6]


# ==================== 第 5 组：斐波那契生成器 ====================
print("\n" + "=" * 50)
print("第 5 组：斐波那契生成器")
print("=" * 50)


def fib(max_count):
    """
    斐波那契数列生成器
    :param max_count: 生成的数列个数
    :yield: 斐波那契数
    """
    a, b = 1, 1
    yield a
    yield b
    for i in range(max_count - 2):
        a, b = b, a + b
        yield b


# 用户输入
count = input("请输入要生成的斐波那契数列的个数：")
count = int(count)

# 使用生成器
fib_generator = fib(count)
print(f"斐波那契数列（前{count}个）：")
for num in fib_generator:
    print(num, end=" ")
print()
