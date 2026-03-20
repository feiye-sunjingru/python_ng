from io import StringIO
from typing import Any, Protocol, TypeVar, runtime_checkable


#  用 Protocol 明确接口
class Drawable(Protocol):
    """协议定义：可绘制的对象"""

    def draw(self) -> None: ...


class Circle:
    """实现了 Drawable 协议的类"""

    def draw(self) -> None:
        print("Drawing a circle")


class Square:
    """实现了 Drawable 协议的类"""

    def draw(self) -> None:
        print("Drawing a square")


class FakeShape:
    """未完全实现 Drawable 协议的类（返回类型不同）"""

    def draw(self) -> str:
        print("Drawing a fake")
        return "fake"


def render(obj: Drawable) -> None:
    """渲染函数：接受任何实现了 draw 方法的对象"""
    obj.draw()


render(Circle())
render(Square())
# draw返回值不同于协议内容
render(FakeShape())  # type: ignore[arg-type]

print("=" * 40)
print("应用场景 1：文件类对象")
print("=" * 40)


class Readable(Protocol):
    """协议定义：可读的对象"""

    def read(self, size: int = -1) -> str: ...


def process_text(source: Readable) -> None:
    """处理文本：接受任何实现了 read 方法的对象"""
    content = source.read(100)
    print(content)


process_text(StringIO("Hello from StringIO!"))

print("=" * 40)
print("应用场景 2：上下文管理器")
print("=" * 40)


T_co = TypeVar("T_co", covariant=True)


#  定义了一个泛型协议
class ContextManager(Protocol[T_co]):
    """协议定义：上下文管理器"""

    def __enter__(self) -> T_co: ...

    def __exit__(self, *args: Any) -> bool | None: ...


def use_resource(cm: ContextManager[str]) -> None:
    """使用资源：接受任何实现了上下文管理器协议的对象"""
    with cm as value:
        print(value.upper())


# StringIO 的 __enter__ 返回自身，不是字符串
# 正确的示例应该使用真正返回字符串的上下文管理器
class StringResource:
    """自定义上下文管理器，返回字符串"""

    def __init__(self, content: str) -> None:
        self.content = content

    def __enter__(self) -> str:
        return self.content

    def __exit__(self, *args: Any) -> bool | None:
        return None


use_resource(StringResource("context manager example"))

print("=" * 40)
print("应用场景 3：验证是否符合协议（运行时）")
print("=" * 40)


# 使用 @runtime_checkable 的 Protocol:
# Python 只会检查对象有没有某个名字的方法（属性），
# 而不会检查这个方法的参数个数、参数类型、返回值类型等是否匹配协议定义。
# 这些只有静态类型检查器（如 mypy）才会验证。
@runtime_checkable
class Drawable2(Protocol):
    def draw(self) -> None: ...


class Circle2:
    def draw(self) -> None: ...


print(isinstance(Circle2(), Drawable2))  # ✅ True
