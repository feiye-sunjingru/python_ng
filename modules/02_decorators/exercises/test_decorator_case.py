# -*- coding: utf-8 -*-
"""
装饰器练习示例
功能：演示多种装饰器的使用场景
"""

# ==================== 导入模块 ====================
import os
import random
from functools import wraps
from pathlib import Path

# ==================== 装饰器定义 ====================


def after(func):
    """后置处理装饰器：在函数执行后打印提示信息"""

    @wraps(func)
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        print("after function call")
        return res

    return inner


def five_times(func):
    """重复执行装饰器：将函数执行 5 次并收集结果"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        res = []
        for _ in range(5):
            res.append(func(*args, **kwargs))
        return res

    return wrapper


def check_path(func):
    """路径检查装饰器：确保输出路径的父目录存在"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        file_path = Path(args[0])
        file_path.parent.mkdir(parents=True, exist_ok=True)
        return func(*args, **kwargs)

    return wrapper


# ==================== 被装饰函数 ====================


@after
def func(a1):
    return a1 + "美女"


@after
def base(a1, a2):
    return a1 + a2 + "靓女"


@after
def base2(a1, a2, a3, a4):
    return a1 + a2 + a3 + a4 + "女神"


@five_times
def func_int():
    return random.randint(1, 4)


@check_path
def write_userinfo(path):
    """写入用户信息到指定文件"""
    with open(path, mode="w", encoding="utf-8") as file_obj:
        file_obj.write("武沛齐")


# ==================== 测试入口 ====================

if __name__ == "__main__":
    print("=" * 40)
    print("测试 after 装饰器")
    print("=" * 40)
    print(func("你是"))
    print(base("你是", "个"))
    print(base2("你是", "个", "大", "漂亮"))

    print("\n" + "=" * 40)
    print("测试 five_times 装饰器")
    print("=" * 40)
    result = func_int()
    print(f"5 次随机结果：{result}")

    print("\n" + "=" * 40)
    print("测试 check_path 装饰器")
    print("=" * 40)
    write_userinfo("tmp_output/bin/xxx.txt")
    print("文件写入完成")
