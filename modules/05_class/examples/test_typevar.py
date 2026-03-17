from typing import Generic, TypeVar

print("=" * 50)
print("场景 1：类型推断 - 保持输入输出类型一致")
print("=" * 50)

T = TypeVar("T")


def first(xs: list[T]) -> T:
    """返回列表的第一个元素，输入输出类型保持一致"""
    return xs[0]


a: int = first([1, 2, 3])  # T 推断为 int
b: str = first(["a", "b", "c"])  # T 推断为 str
c: float = first([1.1, 2.2, 3.3])  # T 推断为 float

print(f"first([1, 2, 3]) = {a} (type: {type(a).__name__})")
print(f"first(['a', 'b', 'c']) = {b} (type: {type(b).__name__})")
print(f"first([1.1, 2.2, 3.3]) = {c} (type: {type(c).__name__})")

print("\n" + "=" * 50)
print("场景 2：类型约束 (bound) - 限制为特定类型的子类")
print("=" * 50)


class Animal:
    def speak(self) -> str:
        return "sound"


class Dog(Animal):
    def speak(self) -> str:
        return "woof"


class Cat(Animal):
    def speak(self) -> str:
        return "meow"


T2 = TypeVar("T2", bound=Animal)


def make_sound(animal: T2) -> T2:
    """接受 Animal 的子类，并返回相同的具体类型"""
    print(f"{animal.__class__.__name__} says: {animal.speak()}")
    return animal


dog = make_sound(Dog())  # 返回类型是 Dog
cat = make_sound(Cat())  # 返回类型是 Cat
print(f"Returned: {dog} (type: {type(dog).__name__})")
print(f"Returned: {cat} (type: {type(cat).__name__})")

print("\n" + "=" * 50)
print("场景 3：类型限定 - 限制为几种特定类型之一")
print("=" * 50)

T3 = TypeVar("T3", int, str)


def duplicate(x: T3) -> T3:
    """只接受 int 或 str，返回相同类型"""
    return x + x


result1 = duplicate(3)  # OK → 6
result2 = duplicate("hi")  # OK → "hihi"
print(f"duplicate(3) = {result1}")
print(f"duplicate('hi') = {result2}")
# duplicate(3.14)  # ❌ 类型检查器会报错！

print("\n" + "=" * 50)
print("场景 4：泛型类 - 类中使用 TypeVar")
print("=" * 50)

T4 = TypeVar("T4")


class Box(Generic[T4]):
    """泛型容器类，可以存储任意类型的值"""

    def __init__(self, content: T4) -> None:
        self.content = content

    def get(self) -> T4:
        return self.content

    def set(self, new_content: T4) -> None:
        self.content = new_content


box1 = Box[int](42)
box2 = Box[str]("hello")
box3 = Box[list]([])

print(f"Box[int]: {box1.get()} (type: {type(box1.get()).__name__})")
print(f"Box[str]: '{box2.get()}' (type: {type(box2.get()).__name__})")
print(f"Box[list]: {box3.get()} (type: {type(box3.get()).__name__})")

box1.set(100)
print(f"After set: Box[int] = {box1.get()}")

print("\n" + "=" * 50)
print("总结")
print("=" * 50)
print("1. 类型推断：T 自动推断，保持输入输出一致")
print("2. 类型约束 (bound)：T 必须是某类型的子类")
print("3. 类型限定：T 只能是指定的几种类型之一")
print("4. 泛型类：在类定义中使用 TypeVar 创建参数化类型")
