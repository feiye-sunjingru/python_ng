"""
Python 参数传递测试

核心结论：
- Python 使用「对象引用传递」
- 可变对象（列表、字典）：函数内修改会影响原对象
- 不可变对象（数字、字符串、元组）：函数内修改不会影响原对象
"""


# ==================== 不可变对象测试 ====================
def test_immutable_objects():
    """测试不可变对象（数字、字符串、元组）"""
    print("=" * 60)
    print("📌 测试 1: 不可变对象（数字）")
    print("=" * 60)

    def modify_num(x):
        """尝试修改数字"""
        print(f"   函数内 - 修改前 id: {id(x)}, 值：{x}")
        x = x + 10
        print(f"   函数内 - 修改后 id: {id(x)}, 值：{x}")

    a = 5
    print(f"调用前 - id: {id(a)}, 值：{a}")
    modify_num(a)
    print(f"调用后 - id: {id(a)}, 值：{a}")
    print("✅ 结论：原对象未改变\n")

    # 字符串测试
    print("=" * 60)
    print("📌 测试 2: 不可变对象（字符串）")
    print("=" * 60)

    def modify_string(s):
        """尝试修改字符串"""
        print(f"   函数内 - 修改前 id: {id(s)}, 值：{s}")
        s = s + " 你好"
        print(f"   函数内 - 修改后 id: {id(s)}, 值：{s}")

    text = "Hello"
    print(f"调用前 - id: {id(text)}, 值：{text}")
    modify_string(text)
    print(f"调用后 - id: {id(text)}, 值：{text}")
    print("✅ 结论：原对象未改变\n")


# ==================== 可变对象测试 ====================


def test_mutable_objects():
    """测试可变对象（列表、字典）"""
    print("=" * 60)
    print("📌 测试 3: 可变对象（列表）- 修改内容")
    print("=" * 60)

    def modify_list(lst):
        """修改列表内容"""
        print(f"   函数内 - 修改前 id: {id(lst)}, 值：{lst}")
        lst.append(4)
        print(f"   函数内 - 修改后 id: {id(lst)}, 值：{lst}")

    my_list = [1, 2, 3]
    print(f"调用前 - id: {id(my_list)}, 值：{my_list}")
    modify_list(my_list)
    print(f"调用后 - id: {id(my_list)}, 值：{my_list}")
    print("⚠️  结论：原对象被改变\n")

    # 字典测试
    print("=" * 60)
    print("📌 测试 4: 可变对象（字典）- 修改内容")
    print("=" * 60)

    def modify_dict(d):
        """修改字典内容"""
        print(f"   函数内 - 修改前 id: {id(d)}, 值：{d}")
        d["age"] = 20
        print(f"   函数内 - 修改后 id: {id(d)}, 值：{d}")

    person = {"name": "小白芽", "age": 18}
    print(f"调用前 - id: {id(person)}, 值：{person}")
    modify_dict(person)
    print(f"调用后 - id: {id(person)}, 值：{person}")
    print("⚠️  结论：原对象被改变\n")


# ==================== 特殊情况测试 ====================


def test_special_cases():
    """测试特殊情况：可变对象重新赋值"""
    print("=" * 60)
    print("📌 测试 5: 可变对象 - 函数内重新赋值")
    print("=" * 60)

    def reassign_list(lst):
        """函数内重新赋值（创建新对象）"""
        print(f"   函数内 - 重新赋值前 id: {id(lst)}, 值：{lst}")
        lst = [10, 20, 30]  # 创建新对象
        print(f"   函数内 - 重新赋值后 id: {id(lst)}, 值：{lst}")

    my_list = [1, 2, 3]
    print(f"调用前 - id: {id(my_list)}, 值：{my_list}")
    reassign_list(my_list)
    print(f"调用后 - id: {id(my_list)}, 值：{my_list}")
    print("✅ 结论：重新赋值不影响原对象\n")

    # 使用切片避免修改原对象
    print("=" * 60)
    print("📌 测试 6: 可变对象 - 使用切片保护原对象")
    print("=" * 60)

    def safe_modify_list(lst):
        """使用切片创建副本后修改"""
        lst_copy = lst[:]  # 或 lst.copy()
        print(f"   函数内 - 副本 id: {id(lst_copy)}, 原列表 id: {id(lst)}")
        lst_copy.append(4)
        print(f"   函数内 - 副本修改后：{lst_copy}")

    my_list = [1, 2, 3]
    print(f"调用前 - 原列表：{my_list}")
    safe_modify_list(my_list)
    print(f"调用后 - 原列表：{my_list}")
    print("✅ 结论：使用副本可保护原对象\n")


# ==================== 总结 ====================


def print_summary():
    """打印总结"""
    print("=" * 60)
    print("📚 Python 参数传递总结")
    print("=" * 60)
    print("""
    核心机制：对象引用传递

    | 对象类型 | 示例              | 函数内修改 | 影响原对象 |
    |----------|-------------------|------------|------------|
    | 不可变   | int, str, tuple   | 创建新对象 | ❌ 否      |
    | 可变     | list, dict, set   | 修改内容   | ✅ 是      |

    安全建议：
    1. 不想影响原对象 → 传递副本（lst.copy() 或 lst[:]）
    2. 函数内避免重新赋值 → 使用返回值
    3. 文档说明是否会修改传入对象
    """)
    print("=" * 60)


# ==================== 主程序 ====================

if __name__ == "__main__":
    test_immutable_objects()
    test_mutable_objects()
    test_special_cases()
    print_summary()
