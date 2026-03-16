# tests/test_match_case.py
"""match case 语法测试用例"""
import pytest


class TestMatchCase:
    """测试 match case 各种场景"""

    def test_match_status_code(self):
        """测试 HTTP 状态码匹配"""
        status = 404
        result = ""

        match status:
            case 200:
                result = "OK"
            case 404:
                result = "Not Found"
            case 500:
                result = "Internal Server Error"
            case _:
                result = "Unknown status"

        assert result == "Not Found"

    def test_match_command(self):
        """测试命令字符串匹配"""
        command = "start"
        result = ""

        match command:
            case "start":
                result = "Starting..."
            case "stop":
                result = "Stopping..."
            case _:
                result = "Unknown command"

        assert result == "Starting..."

    def test_match_tuple_pattern(self):
        """测试元组模式匹配"""
        point = (1, 2)
        result = ""

        match point:
            case (0, 0):
                result = "Origin"
            case (0, y):
                result = f"On Y axis at {y}"
            case (x, 0):
                result = f"On X axis at {x}"
            case (x, y):
                result = f"Point at ({x}, {y})"

        assert result == "Point at (1, 2)"

    def test_match_dict_pattern(self):
        """测试字典模式匹配"""
        user = {"name": "Alice", "role": "admin"}
        result = ""

        match user:
            case {"name": str(name), "role": "admin"}:
                result = f"Admin user: {name}"
            case {"name": str(name)}:
                result = f"Regular user: {name}"

        assert result == "Admin user: Alice"

    def test_match_class_pattern(self):
        """测试类模式匹配"""

        class Point:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        p = Point(1, 2)
        result = ""

        match p:
            case Point(x=0, y=0):
                result = "Origin"
            case Point(x=0, y=y):
                result = f"On Y axis at {y}"
            case Point(x=x, y=y):
                result = f"Point at ({x}, {y})"

        assert result == "Point at (1, 2)"

    def test_match_with_guard(self):
        """测试带条件守卫的模式匹配"""
        point = (3, 4)
        result = ""

        match point:
            case (x, y) if x == y:
                result = "On diagonal"
            case (x, y) if x > y:
                result = "Below diagonal"
            case (x, y):
                result = "Above diagonal"

        assert result == "Above diagonal"

    def test_match_or_pattern(self):
        """测试或模式匹配"""
        status = 500
        result = ""

        match status:
            case 200 | 201 | 202:
                result = "Success"
            case 400 | 401 | 403 | 404:
                result = "Client error"
            case 500 | 502 | 503:
                result = "Server error"

        assert result == "Server error"

    # 每组数据对应一次测试执行
    @pytest.mark.parametrize(
        "status,expected",
        [
            (200, "Success"),
            (201, "Success"),
            (404, "Client error"),
            (500, "Server error"),
            (999, "Unknown"),
        ],
    )
    def test_match_status_parametrized(self, status, expected):
        """参数化测试 HTTP 状态码匹配"""
        result = ""

        match status:
            case 200 | 201 | 202:
                result = "Success"
            case 400 | 401 | 403 | 404:
                result = "Client error"
            case 500 | 502 | 503:
                result = "Server error"
            case _:
                result = "Unknown"

        assert result == expected
