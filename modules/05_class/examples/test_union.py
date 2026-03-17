from typing import Union


# 值联合类型：int或str
# 从 Python 3.10 开始，也可以使用更简洁的写法：int | str
def process(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Number: {value}"
    else:
        return f"Text: {value}"


# 使用示例
print(process(42))  # 输出: Number: 42
print(process("hello"))  # 输出: Text: helloprint(process("hello")) # 输出: Text: hello
# ❌ 类型检查工具会警告（但运行时不报错）
# print(process(3.14))  # 应避免,mypy检查不通过
