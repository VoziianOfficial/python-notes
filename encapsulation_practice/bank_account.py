
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            return False
        else:
            self.__balance += amount
            return True

    def withdraw(self, amount):
        if amount <=0:
            return False
        elif amount > self.__balance:
            return False
        else:
            self.__balance -= amount
            return True