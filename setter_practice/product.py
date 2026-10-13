

class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property 
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Price cannot be negative")
        else:
            self.__price = value



