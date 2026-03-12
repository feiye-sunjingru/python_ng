class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("子类必须实现 speak 方法")


class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"


pets = [Cat("Whiskers"), Dog("Rex")]
for pet in pets:
    print(pet.speak())
