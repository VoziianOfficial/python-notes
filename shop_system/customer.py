class Customer:
    """
    Represents a customer.
    """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        if self.balance < amount:
            return False

        self.balance -= amount
        return True

    def refund(self, amount):
        self.balance += amount

    def show_balance(self):
        return self.balance
