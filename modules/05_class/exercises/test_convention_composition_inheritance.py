from typing import Protocol


# 组合：表达has-a关系，引擎作为汽车的一部分（属性)传递给Car
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"引擎启动，马力：{self.horsepower} 匹")


class Car:
    def __init__(self, brand, engine_horsepower):
        self.brand = brand
        # 使用组合：Car "has-a" Engine
        self.engine = Engine(engine_horsepower)

    def start(self):
        print(f"{self.brand} 汽车准备启动...")
        self.engine.start()  # 委托给 Engine 实例


# 使用示例
my_car = Car("丰田", 150)
my_car.start()

# 定义协议：约定大于继承，有共同的方法或属性


class Playable(Protocol):
    def play(self) -> None: ...


# 两个类无关
class Video:
    def __init__(self, title: str):
        self.title = title

    def play(self) -> None:
        print(f"正在播放视频：{self.title}")


class Audio:
    def __init__(self, name: str):
        self.name = name

    def play(self) -> None:
        print(f"正在播放音频：{self.name}")


def play_media(media: Playable) -> None:
    media.play()


video = Video("Python 教程")
audio = Audio("背景音乐")

play_media(video)  # ✅ 合法：Video 有 play()
play_media(audio)  # ✅ 合法：Audio 有 play()

# 可开关设备


class Switchable(Protocol):
    """约定：只要实现了 turn_on 和 turn_off，就是可开关的设备"""

    def turn_on(self) -> None: ...

    def turn_off(self) -> None: ...


# 不同设备具有开关功能，无需继承
class PhilipsLight:
    def turn_on(self) -> None:
        print("飞利浦灯亮了 💡")

    def turn_off(self) -> None:
        print("飞利浦灯灭了")


class MideaAC:
    def turn_on(self) -> None:
        print("美的空调启动 ❄️")

    def turn_off(self) -> None:
        print("美的空调关闭")


# 控制器里有开关设备：通过组合拥有开关，通过约定可以使用不同设备
class SmartController:
    def __init__(self, device: Switchable):  # ← 依赖约定（接口）
        self.device = device  # ← 使用组合（has-a 关系）

    def power_on(self) -> None:
        self.device.turn_on()  # 委托给组合的对象

    def power_off(self) -> None:
        self.device.turn_off()


light = PhilipsLight()
ac = MideaAC()

# 控制器通过组合 + 约定，适配任意设备
controller1 = SmartController(light)
controller2 = SmartController(ac)

controller1.power_on()  # 飞利浦灯亮了 💡
controller2.power_on()  # 美的空调启动 ❄️
