from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, owner, balance, withdraw_limit):
        self.owner = owner
        self.__balance = balance
        self.__withdraw_limit = withdraw_limit

    @abstractmethod
    def withdraw(self, amount):
        pass 

    def _change_balance(self, amount):
        self.__balance += amount

    @property
    def balance(self):
        return self.__balance

    def deposit(self,amount):
        if amount <= 0:
            return False
        else:
            self.__balance += amount
            return True

    @property
    def withdraw_limit(self):
        return self.__withdraw_limit

    @withdraw_limit.setter
    def withdraw_limit(self, value):
        if value <= 0:
            return False
        else:
            self.__withdraw_limit = value


class DebitAccount(BankAccount):

    def withdraw(self, amount):
        if amount <= 0:
            return False
        if amount > self.withdraw_limit:
            return False

        if amount > self.balance:
            return False

        self._change_balance(-amount)
        return True


class SavingsAccount(BankAccount):

    def __init__(self, owner, balance, withdraw_limit, minimum_balance):
        super().__init__(owner, balance, withdraw_limit)

        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if amount <= 0:
            return False
        if amount > self.withdraw_limit:
            return False

        if self.balance - amount < self.minimum_balance:
            return False

        self._change_balance(-amount)
        return True



class CreditAccount(BankAccount):
    def __init__(self, owner, balance, withdraw_limit, credit_limit):
        super().__init__(owner, balance, withdraw_limit)

        self.credit_limit = credit_limit

    def withdraw(self, amount):
        if amount <= 0:
            return False
        if amount > self.withdraw_limit:
            return False

        if self.balance - amount < -self.credit_limit:
            return False

        self._change_balance(-amount)
        return True