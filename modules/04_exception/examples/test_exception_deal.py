"""
Python 异常处理完整示例
包含：基础异常处理、多种异常捕获、自定义异常、异常链等
"""

import sys
import traceback

# ==================== 第 1 组：基础异常处理 ====================
print("=" * 50)
print("第 1 组：基础异常处理 (try-except-else-finally)")
print("=" * 50)

try:
    value = 8 / 2  # 改为 2，演示正常流程
    print(f"计算结果：{value}")
except ZeroDivisionError:
    print("❌ 除数不能为 0")
else:  # 没有异常时执行
    print("✅ 计算成功，进入 else 分支")
finally:  # 无论是否有异常，都会执行
    print("📌 finally 始终执行，用于清理资源")


# ==================== 第 2 组：捕获多种异常 ====================
print("\n" + "=" * 50)
print("第 2 组：捕获多种异常")
print("=" * 50)


def divide(a, b):
    """除法运算，演示多种异常捕获"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("❌ ZeroDivisionError: 除数不能为 0")
        return None
    except TypeError as e:
        print(f"❌ TypeError: 类型错误 - {e}")
        return None
    except ValueError as e:
        print(f"❌ ValueError: 值错误 - {e}")
        return None
    except Exception as e:
        print(f"❌ 未知异常：{type(e).__name__} - {e}")
        return None


# 测试不同场景
print("测试 1 - 正常除法:", divide(10, 2))
print("测试 2 - 除零错误:", divide(10, 0))
print("测试 3 - 类型错误:", divide(10, "a"))


# ==================== 第 3 组：异常信息记录 ====================
print("\n" + "=" * 50)
print("第 3 组：异常信息记录 (traceback)")
print("=" * 50)

try:
    value = 8 / 0
except ZeroDivisionError:
    print("❌ 捕获到除零异常")

    # 方法 1：打印完整 traceback
    print("\n【方法 1】traceback.format_exc():")
    print("-" * 50)
    info = traceback.format_exc()
    print(info)
    print("-" * 50)

    # 方法 2：打印到 stderr
    print("\n【方法 2】traceback.print_exc():")
    print("-" * 50)
    traceback.print_exc(file=sys.stderr)
    print("-" * 50)

    # 方法 3：获取异常对象信息
    print("\n【方法 3】异常对象信息:")
    print(f"异常类型：{type(value).__name__ if 'value' in dir() else 'ZeroDivisionError'}")
    print(f"异常模块：{ZeroDivisionError.__module__}")


# ==================== 第 4 组：主动抛出异常 ====================
print("\n" + "=" * 50)
print("第 4 组：主动抛出异常 (raise)")
print("=" * 50)


def check_age(age):
    """检查年龄是否合法"""
    if age < 0:
        raise ValueError("年龄不能为负数")
    if age > 150:
        raise ValueError("年龄不能超过 150")
    return True


try:
    check_age(-5)
except ValueError as e:
    print(f"❌ 捕获到 ValueError: {e}")

try:
    check_age(200)
except ValueError as e:
    print(f"❌ 捕获到 ValueError: {e}")

print("✅ check_age(25):", check_age(25))


# ==================== 第 5 组：断言异常 ====================
print("\n" + "=" * 50)
print("第 5 组：断言异常 (AssertionError)")
print("=" * 50)


def validate_data(data):
    """使用断言验证数据"""
    assert isinstance(data, list), "数据必须是列表"
    assert len(data) > 0, "列表不能为空"
    assert all(isinstance(x, (int, float)) for x in data), "所有元素必须是数字"
    return sum(data) / len(data)


# 正常情况
try:
    avg = validate_data([1, 2, 3, 4, 5])
    print(f"✅ 平均值：{avg}")
except AssertionError as e:
    print(f"❌ 断言失败：{e}")

# 异常情况
try:
    validate_data([])  # 空列表
except AssertionError as e:
    print(f"❌ 断言失败：{e}")

try:
    validate_data("not a list")  # 类型错误
except AssertionError as e:
    print(f"❌ 断言失败：{e}")


# ==================== 第 6 组：自定义异常 ====================
print("\n" + "=" * 50)
print("第 6 组：自定义异常")
print("=" * 50)


class InvalidEmailError(Exception):
    """自定义异常：无效邮箱"""

    def __init__(self, email, message="邮箱格式无效"):
        self.email = email
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.email}"


class UserNotFoundError(Exception):
    """自定义异常：用户未找到"""

    pass


def validate_email(email):
    """验证邮箱格式"""
    if "@" not in email or "." not in email:
        raise InvalidEmailError(email)
    return True


def find_user(user_id):
    """查找用户"""
    users = {1: "张三", 2: "李四", 3: "王五"}
    if user_id not in users:
        raise UserNotFoundError(f"用户 ID {user_id} 不存在")
    return users[user_id]


# 测试自定义异常
try:
    validate_email("invalid-email")
except InvalidEmailError as e:
    print(f"❌ {e}")

try:
    find_user(999)
except UserNotFoundError as e:
    print(f"❌ {e}")

print("✅ validate_email('test@example.com'):", validate_email("test@example.com"))
print("✅ find_user(1):", find_user(1))


# ==================== 第 7 组：异常链 ====================
print("\n" + "=" * 50)
print("第 7 组：显式异常链 (raise ... from ...)")
print("=" * 50)


class DatabaseError(Exception):
    """数据库异常"""

    pass


def query_database(sql):
    """模拟数据库查询"""
    try:
        # 模拟底层异常
        raise ValueError("SQL 语法错误")
    except ValueError as e:
        # 包装为业务异常，保留原始异常链
        raise DatabaseError(f"查询失败：{sql}") from e


try:
    query_database("SELECT * FROM users")
except DatabaseError as e:
    print(f"❌ 捕获到 DatabaseError: {e}")
    print(f"📎 原始异常：{e.__cause__}")


# ==================== 第 8 组：最佳实践 ====================
print("\n" + "=" * 50)
print("第 8 组：异常处理最佳实践")
print("=" * 50)

best_practices = """
✅ 推荐做法：
1. 只捕获能处理的异常，不要盲目捕获所有异常
2. 使用具体的异常类型，而不是 bare except
3. finally 用于资源清理（关闭文件、释放连接等）
4. 自定义异常让错误更明确
5. 使用异常链保留原始错误信息

❌ 避免做法：
1. except: 或 except Exception: 捕获所有异常
2. 在 except 中 pass 忽略所有错误
3. 用异常处理代替正常的条件判断
4. 过深的 try-except 嵌套
"""
print(best_practices)


# ==================== 第 9 组：资源管理 (with 语句) ====================
print("\n" + "=" * 50)
print("第 9 组：资源管理 (with 语句)")
print("=" * 50)

# 自动资源管理，无需手动 close
try:
    with open("test_exception.txt", "w", encoding="utf-8") as f:
        f.write("测试内容")
    print("✅ 文件写入成功，自动关闭")

    with open("test_exception.txt", "r", encoding="utf-8") as f:
        content = f.read()
    print(f"✅ 文件读取成功：{content}")
except IOError as e:
    print(f"❌ 文件操作异常：{e}")
finally:
    # 清理测试文件
    import os

    if os.path.exists("test_exception.txt"):
        os.remove("test_exception.txt")
        print("🧹 测试文件已清理")
