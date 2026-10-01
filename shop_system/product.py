class Product:
    """
    Represents a product in the shop.
    """
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Stock: {self.stock}")

    def is_available(self,quantity):
        if self.stock >= quantity:
            return True
        else:
            return False

    def reduce_stock(self, quantity):
        self.stock -= quantity

    def restore_stock(self, quantity):
        self.stock += quantity

