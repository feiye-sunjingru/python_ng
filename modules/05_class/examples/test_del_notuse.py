import sys


class Resource:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} 被销毁")
        # 假设这里要关闭文件、网络连接等


r = Resource("my_resource")

# 强制退出: Python 解释器开始关闭,模块和全局变量会被清理，
# 但此时很多内置对象（如 print、sys）可能已经被销毁, 因此可能无输出
sys.exit()
