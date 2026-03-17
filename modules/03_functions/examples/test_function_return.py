"""
Python 函数返回值与对象缓存机制测试

测试目的：
- 验证函数返回不同对象类型时的内存行为
- 理解 Python 的缓存和驻留机制
- 区分可变对象与不可变对象的差异
"""

# ==================== 可变对象测试 ====================


def test_mutable_objects():
    """测试可变对象（列表、字典等）"""
    print("=" * 60)
    print("📌 测试 1: 可变对象 - 列表")
    print("=" * 60)

    def get_list():
        """返回新列表"""
        return [1, 2, 3]

    l1 = get_list()
    l2 = get_list()

    print(f"l1 id: {id(l1)}, 值：{l1}")
    print(f"l2 id: {id(l2)}, 值：{l2}")
    print(f"l1 is l2: {l1 is l2}")
    print("✅ 结论：每次调用创建新对象，内存地址不同\n")


# ==================== 不可变对象测试 ====================


def test_immutable_objects():
    """测试不可变对象（数字、字符串、元组）"""

    # 整数缓存
    print("=" * 60)
    print("📌 测试 2: 不可变对象 - 整数（缓存范围 -5~256）")
    print("=" * 60)

    def get_num():
        """返回整数"""
        return 100

    a = get_num()
    b = get_num()

    print(f"a id: {id(a)}, 值：{a}")
    print(f"b id: {id(b)}, 值：{b}")
    print(f"a is b: {a is b}")
    print("✅ 结论：小整数被缓存，复用同一对象\n")

    # 字符串驻留
    print("=" * 60)
    print("📌 测试 3: 不可变对象 - 字符串（驻留机制）")
    print("=" * 60)

    def get_str():
        """返回字符串"""
        return "hello"

    s1 = get_str()
    s2 = get_str()

    print(f"s1 id: {id(s1)}, 值：{s1}")
    print(f"s2 id: {id(s2)}, 值：{s2}")
    print(f"s1 is s2: {s1 is s2}")
    print("✅ 结论：相同字符串被 intern，复用同一对象\n")

    # 动态字符串
    print("=" * 60)
    print("📌 测试 4: 字符串 - 编译时优化 vs 运行时拼接")
    print("=" * 60)

    def get_dyn_str():
        """编译时可确定的字符串"""
        return "he" + "llo"

    def get_dyn_str2():
        """运行时拼接的字符串"""
        return "he".join(["l", "lo"])

    d1 = get_dyn_str()
    d2 = get_dyn_str()
    print(f"编译时优化：get_dyn_str() is get_dyn_str() = {d1 is d2}")

    r1 = get_dyn_str2()
    r2 = get_dyn_str2()
    print(f"运行时拼接：get_dyn_str2() is get_dyn_str2() = {r1 is r2}")
    print("✅ 结论：编译时优化可能 intern，运行时拼接通常不 intern\n")


# ==================== 特殊对象测试 ====================


def test_special_objects():
    """测试特殊对象（空元组、None 等）"""
    print("=" * 60)
    print("📌 测试 5: 特殊对象 - 空元组（单例）")
    print("=" * 60)

    def get_empty_tuple():
        """返回空元组"""
        return ()

    t1 = get_empty_tuple()
    t2 = get_empty_tuple()

    print(f"t1 id: {id(t1)}, 值：{t1}")
    print(f"t2 id: {id(t2)}, 值：{t2}")
    print(f"t1 is t2: {t1 is t2}")
    print("✅ 结论：空元组是单例，全局只有一个对象\n")

    # None 测试
    print("=" * 60)
    print("📌 测试 6: 特殊对象 - None（单例）")
    print("=" * 60)

    def get_none():
        """返回 None"""
        return None

    n1 = get_none()
    n2 = get_none()

    print(f"n1 id: {id(n1)}, 值：{n1}")
    print(f"n2 id: {id(n2)}, 值：{n2}")
    print(f"n1 is n2: {n1 is n2}")
    print("✅ 结论：None 是单例，全局只有一个对象\n")


# ==================== 对比测试 ====================


def test_comparison():
    """对比测试：可变 vs 不可变"""
    print("=" * 60)
    print("📌 测试 7: 对比 - 可变对象 vs 不可变对象")
    print("=" * 60)

    # 列表（可变）
    def get_list():
        return [1, 2, 3]

    # 元组（不可变）
    def get_tuple():
        return (1, 2, 3)

    list1 = get_list()
    list2 = get_list()
    tuple1 = get_tuple()
    tuple2 = get_tuple()

    print(f"列表：get_list() is get_list() = {list1 is list2}")
    print(f"元组：get_tuple() is get_tuple() = {tuple1 is tuple2}")
    print("✅ 结论：可变对象每次新建，不可变对象可能复用\n")


# ==================== 总结 ====================


def print_summary():
    """打印总结"""
    print("=" * 60)
    print("📚 Python 对象缓存机制总结")
    print("=" * 60)
    print("""
    | 对象类型      | 示例           | 缓存/驻留 | 多次返回是否同一对象 |
    |---------------|----------------|-----------|---------------------|
    | 小整数        | -5 ~ 256       | ✅ 缓存   | 是（同一 ID）        |
    | 大整数        | > 256 或 < -5  | ❌ 不缓存 | 通常否              |
    | 字符串字面量  | "hello"        | ✅ 驻留   | 是（同一 ID）        |
    | 动态字符串    | 运行时拼接     | ❌ 不驻留 | 通常否              |
    | 列表          | [1, 2, 3]      | ❌ 不缓存 | 否（每次新建）       |
    | 空元组        | ()             | ✅ 单例   | 是（同一 ID）        |
    | 非空元组      | (1, 2, 3)      | ❌ 不缓存 | 通常否              |
    | None          | None           | ✅ 单例   | 是（同一 ID）        |

    核心机制：
    1. 整数缓存：-5 到 256 范围内的整数被预先创建并复用
    2. 字符串驻留：相同字符串字面量共享同一对象
    3. 单例对象：None、空元组、空字符串等全局唯一
    4. 可变对象：每次创建新对象，保证独立性
    """)
    print("=" * 60)


# ==================== 主程序 ====================

if __name__ == "__main__":
    test_mutable_objects()
    test_immutable_objects()
    test_special_objects()
    test_comparison()
    print_summary()
