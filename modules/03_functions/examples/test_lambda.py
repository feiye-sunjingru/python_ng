"""
Lambda 表达式测试模块
功能：演示和测试 lambda 表达式的各种使用场景
"""

# ==================== 导入模块 ====================
import unittest
from functools import reduce

# ==================== 测试类 ====================


class TestLambda(unittest.TestCase):
    """Lambda 表达式测试类"""

    def test_lambda_basic(self):
        """测试 lambda 基础语法"""
        add = lambda x, y: x + y  # noqa: E731
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(10, 20), 30)

    def test_lambda_with_no_args(self):
        """测试 lambda 无参数"""
        greet = lambda: "Hello, World!"  # noqa: E731
        self.assertEqual(greet(), "Hello, World!")

    def test_lambda_with_map(self):
        """测试 lambda 与 map 函数配合"""
        numbers = [1, 2, 3, 4, 5]
        squared = list(map(lambda x: x**2, numbers))  # noqa: C417
        self.assertEqual(squared, [1, 4, 9, 16, 25])

    def test_lambda_with_filter(self):
        """测试 lambda 与 filter 函数配合"""
        numbers = [1, 2, 3, 4, 5, 6]
        evens = list(filter(lambda x: x % 2 == 0, numbers))
        self.assertEqual(evens, [2, 4, 6])

    def test_lambda_with_reduce(self):
        """测试 lambda 与 reduce 函数配合"""
        numbers = [1, 2, 3, 4, 5]
        total = reduce(lambda x, y: x + y, numbers)
        self.assertEqual(total, 15)

    def test_lambda_with_sort(self):
        """测试 lambda 用于排序"""
        pairs = [(1, "one"), (3, "three"), (2, "two")]
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        self.assertEqual(sorted_pairs, [(1, "one"), (3, "three"), (2, "two")])

    def test_lambda_multiple_args(self):
        """测试 lambda 多参数"""
        multiply = lambda x, y, z: x * y * z  # noqa: E731
        self.assertEqual(multiply(2, 3, 4), 24)

    def test_lambda_default_args(self):
        """测试 lambda 默认参数"""
        power = lambda x, n=2: x**n  # noqa: E731
        self.assertEqual(power(3), 9)
        self.assertEqual(power(3, 3), 27)

    def test_lambda_closure(self):
        """测试 lambda 闭包"""

        def make_multiplier(n):
            return lambda x: x * n

        double = make_multiplier(2)
        triple = make_multiplier(3)

        self.assertEqual(double(5), 10)
        self.assertEqual(triple(5), 15)

    def test_lambda_with_if_else(self):
        """测试 lambda 中的条件表达式"""
        classify = lambda x: "正数" if x > 0 else ("零" if x == 0 else "负数")  # noqa: E731
        self.assertEqual(classify(10), "正数")
        self.assertEqual(classify(0), "零")
        self.assertEqual(classify(-5), "负数")

    def test_lambda_with_closure_error(self):
        """测试 lambda 闭包中变量捕获问题"""
        funcs = [lambda x: x + i for i in range(3)]  # noqa: B023
        results = [f(0) for f in funcs]
        self.assertEqual(results, [2, 2, 2])  # ❌ 错误结果，i 的值被捕获为最后一个值

        # 正确写法：绑定当前 i 的值
        funcs = [lambda x, i=i: x + i for i in range(3)]
        results = [f(0) for f in funcs]
        self.assertEqual(results, [0, 1, 2])  # ✅ 正确结果，i 的值被正确绑定


# ==================== 测试入口 ====================

if __name__ == "__main__":
    # 运行测试
    unittest.main(verbosity=2)
