# 封装 (@property + 私有属性) 使用示例


class BankAccount:
    """银行账户 - 演示封装特性"""

    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.__balance = balance  # 私有属性（名称改写）

    def deposit(self, amount: float) -> None:
        """存款操作"""
        if amount > 0:
            self.__balance += amount

    def get_balance(self) -> float:
        """获取余额（只读访问）"""
        return self.__balance


# 使用示例
acc = BankAccount("Alice")
acc.deposit(100)
print(acc.get_balance())  # 输出: 100
# print(acc.__balance)      # ❌ AttributeError
# print(acc._BankAccount__balance)  # ✅ 可访问（但不推荐）
