"""
可变参数测试模块
测试 *args 和 **kwargs 的使用场景
"""

import pytest


class TestArgs:
    """*args 位置可变参数测试"""

    def test_args_basic(self):
        """测试基础位置参数接收"""

        def my_func(*args):
            return args

        result = my_func(1, 2, 3, "hello")
        assert result == (1, 2, 3, "hello")
        assert isinstance(result, tuple)

    def test_args_empty(self):
        """测试无参数情况"""

        def my_func(*args):
            return args

        assert my_func() == ()

    def test_args_single(self):
        """测试单个参数"""

        def my_func(*args):
            return args

        assert my_func(42) == (42,)


class TestKwargs:
    """**kwargs 关键字可变参数测试"""

    def test_kwargs_basic(self):
        """测试基础关键字参数接收"""

        def my_func(**kwargs):
            return kwargs

        result = my_func(name="Alice", age=25, city="Beijing")
        assert result == {"name": "Alice", "age": 25, "city": "Beijing"}
        assert isinstance(result, dict)

    def test_kwargs_empty(self):
        """测试无关键字参数情况"""

        def my_func(**kwargs):
            return kwargs

        assert my_func() == {}


class TestArgsAndKwargs:
    """*args 和 **kwargs 混合使用测试"""

    def test_mixed_params(self):
        """测试混合参数接收"""

        def greet(greeting, *args, **kwargs):
            return {"greeting": greeting, "args": args, "kwargs": kwargs}

        result = greet("Hello", "Tom", "Jerry", lang="en", time="morning")
        assert result["greeting"] == "Hello"
        assert result["args"] == ("Tom", "Jerry")
        assert result["kwargs"] == {"lang": "en", "time": "morning"}

    def test_required_and_optional(self):
        """测试必需参数与可变参数组合"""

        def func(required, *args, **kwargs):
            return required, args, kwargs

        result = func("must", 1, 2, key="value")
        assert result[0] == "must"
        assert result[1] == (1, 2)
        assert result[2] == {"key": "value"}


class TestUnpacking:
    """参数解包测试"""

    def test_list_unpacking(self):
        """测试列表解包 *"""

        def add(a, b, c):
            return a + b + c

        nums = [1, 2, 3]
        assert add(*nums) == 6

    def test_dict_unpacking(self):
        """测试字典解包 **"""

        def add(a, b, c):
            return a + b + c

        info = {"a": 10, "b": 20, "c": 30}
        assert add(**info) == 60

    def test_unpacking_mixed(self):
        """测试混合解包"""

        def func(a, b, c, d):
            return a + b + c + d

        args = [1, 2]
        kwargs = {"c": 3, "d": 4}
        assert func(*args, **kwargs) == 10


# ==================== 字符串格式化测试 ====================


def test_string_formatting():
    """测试字符串格式化（与参数传递无关，单独测试）"""
    print("=" * 60)
    print("📌 测试 7: 字符串格式化")
    print("=" * 60)

    # 位置参数
    print("我叫{},今年{}岁了！".format("小白芽", 18))
    print("我叫{},今年{}岁了！".format(*["小白芽", 18]))

    # 关键字参数
    print("我叫{name},今年{age}岁了！".format(name="小白芽", age=18))
    print("我叫{name},今年{age}岁了！".format(**{"name": "小白芽", "age": 18}))
    print()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
    test_string_formatting()
