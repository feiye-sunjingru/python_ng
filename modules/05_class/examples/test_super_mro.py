class A:
    def speak(self):
        print("A")


class B(A):
    def speak(self):
        print("B")
        # MRO链下一个是C
        super().speak()


class C(A):
    def speak(self):
        print("C")
        # MRO链下一个是A
        super().speak()


class D(B, C):
    def speak(self):
        print("D")
        # 注意：super() 并不是直接调用“父类”，而是调用 MRO 中的下一个类B
        super().speak()


# 创建类 D(B, C) 时，Python 使用 C3 线性化算法 来确定D的 MRO
d = D()
d.speak()
print(D.__mro__)
