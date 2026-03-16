def func(a1, a2=[1, 2]):
    """函数定义 - 可变默认参数"""
    a2.append(a1)
    return a2


def func1(a1, a2=None):
    """函数定义 - 不可变默认参数"""
    if a2 is None:
        a2 = [1, 2]
    a2.append(a1)
    return a2


def func2(*args, **kwargs):
    """函数定义 - 可变参数"""
    return args


class TestDefaultParam:
    def test_func_default_param_variable(self):
        """测试默认参数可变：内部修改默认参数会影响后续调用"""
        assert func(3) == [1, 2, 3]
        assert func(4) == [1, 2, 3, 4]
        assert func(5) == [1, 2, 3, 4, 5]
        assert func(6) == [1, 2, 3, 4, 5, 6]
        assert func(7, [10, 20]) == [10, 20, 7]
        assert func(8) == [1, 2, 3, 4, 5, 6, 8]

    def test_func1_default_param_immutable(self):
        """测试默认参数不可变：内部修改默认参数不会影响后续调用"""
        assert func1(3) == [1, 2, 3]
        assert func1(4) == [1, 2, 4]
        assert func1(5) == [1, 2, 5]
        assert func1(6) == [1, 2, 6]
        assert func1(7, [10, 20]) == [10, 20, 7]
        assert func1(8) == [1, 2, 8]

    def test_func2_default_param_variable(self):
        """测试默认参数可变：可变参数"""
        params = {"key1": "value1", "key2": "value2"}
        assert func2(params) == ({"key1": "value1", "key2": "value2"},)
        assert func2(*params) == ("key1", "key2")
        assert func2(**params) == ()
