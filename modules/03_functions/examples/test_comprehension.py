import time
from typing import Any

"""
Python 推导式与生成器示例
包含：列表推导式、字典推导式、集合推导式、生成器表达式
"""

# ==================== 第 1 组：基础列表推导式 ====================
print("=" * 50)
print("第 1 组：基础列表推导式")
print("=" * 50)

# 传统写法 vs 推导式写法
# 传统写法
squares = []
for i in range(10):
    squares.append(i**2)
print(f"传统写法：{squares}")

# 推导式写法
squares = [i**2 for i in range(10)]
print(f"推导式写法：{squares}")

# 字符串转大写
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"转大写：{upper_words}")  # ['HELLO', 'WORLD', 'PYTHON']


# ==================== 第 2 组：带条件的列表推导式 ====================
print("\n" + "=" * 50)
print("第 2 组：带条件的列表推导式")
print("=" * 50)

# 筛选偶数
evens = [i for i in range(20) if i % 2 == 0]
print(f"20 以内的偶数：{evens}")

# 筛选能被 3 整除的数
multiples_of_3 = [i for i in range(20) if i % 3 == 0]
print(f"能被 3 整除：{multiples_of_3}")

# 多条件筛选
numbers = [i for i in range(50) if i % 2 == 0 if i % 5 == 0]
print(f"能被 2 和 5 整除：{numbers}")  # [0, 10, 20, 30, 40]

# 条件表达式（if-else）
result = [x if x > 5 else 0 for x in range(10)]
print(f"大于 5 保留，否则为 0：{result}")


# ==================== 第 3 组：嵌套列表推导式 ====================
print("\n" + "=" * 50)
print("第 3 组：嵌套列表推导式")
print("=" * 50)

# 二维列表展平
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"二维展平：{flattened}")  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 创建乘法表
multiplication = [[f"{i} * {j}" for j in range(1, 10)] for i in range(1, 10)]
print(f"乘法表第一行：{multiplication[0]}")

# 配对组合
pairs = [(x, y) for x in range(3) for y in range(3)]
print(f"坐标配对：{pairs}")


# ==================== 第 4 组：字典推导式 ====================
print("\n" + "=" * 50)
print("第 4 组：字典推导式")
print("=" * 50)

# 列表转字典
keys = ["a", "b", "c", "d"]
values = [1, 2, 3, 4]
# d = dict(zip(keys, values, strict=True))
d = {k: v for k, v in zip(keys, values, strict=True)}  # noqa: C416
print(f"zip 转字典：{d}")

# 平方字典
squares_dict = {x: x**2 for x in range(5)}
print(f"平方字典：{squares_dict}")  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 过滤字典
info = {"name": "张三", "age": 25, "city": "北京", "score": 90}
filtered = {k: v for k, v in info.items() if isinstance(v, int)}
print(f"只保留整数：{filtered}")  # {'age': 25, 'score': 90}

# 交换键值
swapped = {v: k for k, v in d.items()}
print(f"键值交换：{swapped}")


# ==================== 第 5 组：集合推导式 ====================
print("\n" + "=" * 50)
print("第 5 组：集合推导式")
print("=" * 50)

# 去重并计算平方
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares = {x**2 for x in numbers}
print(f"去重平方：{unique_squares}")  # {1, 4, 9, 16}

# 提取字符串中的唯一字符
text = "hello world"
unique_chars = {char for char in text if char != " "}
print(f"唯一字符：{unique_chars}")  # {'h', 'e', 'l', 'o', 'w', 'r', 'd'}

# 筛选偶数集合
even_set = {x for x in range(20) if x % 2 == 0}
print(f"偶数集合：{even_set}")


# ==================== 第 6 组：生成器表达式 ====================
print("\n" + "=" * 50)
print("第 6 组：生成器表达式")
print("=" * 50)

# 生成器 vs 列表推导式
# 列表推导式（立即生成，占用内存）
list_comp = [x**2 for x in range(1000000)]
print(f"列表类型：{type(list_comp)}")  # <class 'list'>

# 生成器表达式（惰性求值，节省内存）
gen_expr = (x**2 for x in range(1000000))
print(f"生成器类型：{type(gen_expr)}")  # <class 'generator'>

# 生成器使用
gen = (x for x in range(5))
print("生成器遍历：", end="")
for num in gen:
    print(num, end=" ")
print()

# 生成器求和（无需创建中间列表）
total = sum(x**2 for x in range(10))
print(f"平方和：{total}")  # 285


# ==================== 第 7 组：实际应用场景 ====================
print("\n" + "=" * 50)
print("第 7 组：实际应用场景")
print("=" * 50)

# 1. 提取嵌套数据
users: list[dict[str, Any]] = [
    {"name": "张三", "age": 25, "skills": ["Python", "Java"]},
    {"name": "李四", "age": 30, "skills": ["Python", "Go"]},
    {"name": "王五", "age": 28, "skills": ["Java", "Go"]},
]

# 提取所有用户名
names = [user["name"] for user in users]
print(f"用户名：{names}")

# 提取所有技能（去重）
all_skills = {skill for user in users for skill in user["skills"]}
print(f"所有技能：{all_skills}")

# 2. 过滤有效数据
data = [10, None, 20, "", 30, 0, 40, False, 50]
valid_data = [x for x in data if x]
print(f"有效数据：{valid_data}")  # [10, 20, 30, 40, 50]

# 3. 字符串处理
sentences = ["Hello World", "Python Is Great", "Code Daily"]
word_lengths = [len(word) for sentence in sentences for word in sentence.split()]
print(f"单词长度：{word_lengths}")

# 4. 矩阵转置
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
print(f"矩阵转置：{transposed}")


# ==================== 第 8 组：性能对比 ====================
print("\n" + "=" * 50)
print("第 8 组：性能对比")
print("=" * 50)


# 传统循环
start = time.time()
result = []
for i in range(100000):
    if i % 2 == 0:
        result.append(i**2)
time_loop = time.time() - start

# 列表推导式
start = time.time()
result = [i**2 for i in range(100000) if i % 2 == 0]
time_comp = time.time() - start

print(f"传统循环耗时：{time_loop:.4f} 秒")
print(f"列表推导式耗时：{time_comp:.4f} 秒")
print(f"推导式提速：{time_loop / time_comp:.2f} 倍")
print(f"推导式提速：{time_loop / time_comp:.2f} 倍")
print(f"推导式提速：{time_loop / time_comp:.2f} 倍")
