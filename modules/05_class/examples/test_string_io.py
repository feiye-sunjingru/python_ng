# test_string_io.py
# StringIO 使用示例与测试

import csv
from io import StringIO

# ==================== 基础用法 ====================


def test_basic_write():
    """基础写入操作"""
    s = StringIO()
    s.write("Hello, ")
    s.write("world!")
    print(f"基础写入：{s.getvalue()}")  # Hello, world!
    s.close()


def test_basic_read():
    """基础读取操作"""
    s2 = StringIO("Line 1\nLine 2\nLine 3")
    print("逐行读取：")
    for line in s2:
        print(f"  {repr(line)}")
    s2.close()


# ==================== 测试场景 ====================


def test_file_simulation():
    """模拟文件输入/输出进行测试"""

    def process_file(file_obj):
        return file_obj.read().upper()

    input_data = StringIO("hello")
    result = process_file(input_data)
    assert result == "HELLO", f"期望 'HELLO', 得到 '{result}'"
    print("文件模拟测试：✅ 通过")
    input_data.close()


def test_string_concatenation():
    """高效字符串拼接（替代 +=）"""
    buf = StringIO()
    for i in range(1000):
        buf.write(f"item {i}\n")
    result = buf.getvalue()
    print(f"字符串拼接：{len(result.splitlines())} 行")
    buf.close()


# ==================== 模块配合 ====================


def test_csv_integration():
    """与 csv 模块配合使用"""
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 30])
    print(f"CSV 输出：\n{output.getvalue()}")
    output.close()


# ==================== 指针操作 ====================


def test_pointer_operations():
    """文件指针操作演示"""
    s = StringIO("Hello\nWorld\n")

    # 读取后指针移动到末尾
    content1 = s.read()
    print(f"第一次读取：{repr(content1)}")  # 'Hello\nWorld\n'

    # 再次读取为空（指针已在末尾）
    content2 = s.read()
    print(f"第二次读取：{repr(content2)}")  # ''

    # getvalue() 始终返回完整内容
    print(f"getvalue()：{repr(s.getvalue())}")  # 'Hello\nWorld\n'

    # 移动指针到中间
    s.seek(6)  # 指向 'W'
    print(f"seek(6) 后读取：{repr(s.read())}")  # 'World\n'

    # getvalue() 仍返回完整内容
    print(f"getvalue() 仍完整：{repr(s.getvalue())}")  # 'Hello\nWorld\n'

    s.close()


# ==================== 主程序 ====================

if __name__ == "__main__":
    print("=" * 50)
    print("StringIO 使用示例")
    print("=" * 50)

    test_basic_write()
    print()

    test_basic_read()
    print()

    test_file_simulation()
    print()

    test_string_concatenation()
    print()

    test_csv_integration()
    print()

    test_pointer_operations()
    print()

    print("=" * 50)
    print("所有测试完成")
    print("=" * 50)
