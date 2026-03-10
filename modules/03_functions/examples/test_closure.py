# test_modules.py
"""Python 闭包与作用域测试模块"""
import unittest

# 全局变量
name = "武涛齐"
global_counter = 0


def run():
    """创建闭包函数"""
    name = "alex"

    def inner():
        return name

    return inner


def run_with_counter():
    """带计数器的闭包示例"""
    counter = 0

    def increment():
        nonlocal counter
        counter += 1
        return counter

    return increment


class TestClosureAndScope(unittest.TestCase):
    """闭包与作用域测试类"""

    def test_global_variable_access(self):
        """测试全局变量可直接访问"""
        self.assertEqual(name, "武涛齐")

    def test_closure_captures_enclosing_scope(self):
        """测试闭包捕获外层作用域变量"""
        v1 = run()
        self.assertEqual(v1(), "alex")

    def test_closure_independence(self):
        """测试多个闭包实例相互独立"""
        v1 = run()
        v2 = run()
        self.assertEqual(v1(), v2())
        self.assertIsNot(v1, v2)

    def test_closure_with_nonlocal(self):
        """测试 nonlocal 关键字修改外层变量"""
        counter_func = run_with_counter()
        self.assertEqual(counter_func(), 1)
        self.assertEqual(counter_func(), 2)
        self.assertEqual(counter_func(), 3)

    def test_multiple_counters_independent(self):
        """测试多个计数器闭包独立"""
        counter1 = run_with_counter()
        counter2 = run_with_counter()
        self.assertEqual(counter1(), 1)
        self.assertEqual(counter2(), 1)  # 独立计数
        self.assertEqual(counter1(), 2)
        self.assertEqual(counter2(), 2)


class TestScopeRules(unittest.TestCase):
    """作用域规则测试类"""

    def test_legb_rule(self):
        """测试 LEGB 作用域查找规则"""
        # Local -> Enclosing -> Global -> Built-in
        def outer():
            x = "enclosing"

            def inner():
                return x  # 访问 Enclosing 作用域

            return inner

        self.assertEqual(outer()(), "enclosing")

    def test_global_keyword(self):
        """测试 global 关键字"""
        global global_counter
        original = global_counter
        global_counter += 1
        self.assertEqual(global_counter, original + 1)


if __name__ == "__main__":
    unittest.main()
