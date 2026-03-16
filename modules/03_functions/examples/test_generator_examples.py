# -*- coding: utf-8 -*-
"""
生成器测试模块
功能：演示和测试生成器函数的各种使用场景
"""

import os
import tempfile

# ==================== 导入模块 ====================
import unittest

# ==================== 生成器函数定义 ====================


def count_up_to(n):
    """计数生成器：从 1 计数到 n"""
    i = 1
    while i <= n:
        yield i
        i += 1


def echo():
    """回声生成器：接收并打印发送的值"""
    while True:
        received = yield
        print(f"收到：{received}")


def read_large_file(file_path):
    """文件行读取生成器：逐行读取文件内容"""
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def fibonacci():
    """斐波那契数列生成器：无限生成斐波那契数"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# ==================== 测试类 ====================


class TestGenerator(unittest.TestCase):
    """生成器测试类"""

    def test_count_up_to_basic(self):
        """测试计数生成器基础功能"""
        gen = count_up_to(5)
        result = list(gen)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_count_up_to_iteration(self):
        """测试计数生成器迭代行为"""
        gen = count_up_to(3)
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 2)
        self.assertEqual(next(gen), 3)

    def test_count_up_to_exhausted(self):
        """测试生成器耗尽后抛出 StopIteration"""
        gen = count_up_to(1)
        next(gen)
        with self.assertRaises(StopIteration):
            next(gen)

    def test_generator_expression_basic(self):
        """测试生成器表达式基础功能"""
        gen = (x**2 for x in range(5))
        self.assertEqual(list(gen), [0, 1, 4, 9, 16])

    def test_generator_expression_filter(self):
        """测试生成器表达式带过滤条件"""
        nums = range(10)
        evens = (x for x in nums if x % 2 == 0)
        squares = (x**2 for x in evens)
        self.assertEqual(list(squares), [0, 4, 16, 36, 64])

    def test_generator_send(self):
        """测试生成器 send 方法发送值"""
        g = echo()
        next(g)  # 启动生成器
        # 注意：send 会返回值，这里主要测试不报错
        self.assertIsNone(g.send("你好"))
        self.assertIsNone(g.send("Python"))
        g.close()  # 清理生成器

    def test_read_large_file(self):
        """测试文件读取生成器"""
        # 创建临时文件
        with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8") as f:
            f.write("line1\nline2\nline3\n")
            temp_path = f.name

        try:
            lines = list(read_large_file(temp_path))
            self.assertEqual(lines, ["line1", "line2", "line3"])
        finally:
            os.unlink(temp_path)  # 清理临时文件

    def test_fibonacci_sequence(self):
        """测试斐波那契数列生成器"""
        gen = fibonacci()
        result = [next(gen) for _ in range(7)]
        self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8])

    def test_fibonacci_independence(self):
        """测试多个生成器实例相互独立"""
        gen1 = fibonacci()
        gen2 = fibonacci()
        self.assertEqual(next(gen1), 0)
        self.assertEqual(next(gen2), 0)
        self.assertEqual(next(gen1), 1)
        self.assertEqual(next(gen2), 1)

    def test_generator_memory_efficiency(self):
        """测试生成器内存效率（惰性求值）"""
        gen = (x for x in range(1000000))
        # 生成器对象不会立即计算所有值
        self.assertIsNotNone(gen)
        # 只取前 5 个值
        first_five = [next(gen) for _ in range(5)]
        self.assertEqual(first_five, [0, 1, 2, 3, 4])


# ==================== 测试入口 ====================

if __name__ == "__main__":
    # 运行测试
    unittest.main(verbosity=2)
