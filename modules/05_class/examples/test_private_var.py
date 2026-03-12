class MyClass:
    def __init__(self):
        self.__private = 42
        self._age = 24


obj = MyClass()
# Python没有真正的私有：而是通过名称改写或者约定来让开发者知晓“这个变量/方法是内部的，请勿直接使用”
print(obj._MyClass__private)  # 输出: 42
print(obj._age)  # 输出: 24
