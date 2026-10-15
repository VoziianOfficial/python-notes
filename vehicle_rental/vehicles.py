from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand, model, price_per_day):
        self.brand = brand
        self.model = model
        self.__price_per_day = price_per_day

    @property
    def price_per_day(self):
        return self.__price_per_day

    @price_per_day.setter
    def price_per_day(self, value):
        if value <= 0:
            return
       
        self.__price_per_day = value

    @abstractmethod
    def calculate_price(self, days):
        pass


class Car(Vehicle):
        def __init__(self, brand, model, price_per_day):
            super().__init__(brand, model, price_per_day)

        def calculate_price(self,days):
             if days <= 0:
                  return 0

             return self.price_per_day * days


class Bike(Vehicle):
    def __init__(self, brand, model, price_per_day):
        super().__init__(brand, model, price_per_day)

    def calculate_price(self, days):
        if days <= 0:
            return 0

        return self.price_per_day * days
    

class Scooter(Vehicle):
    def __init__(self, brand, model, price_per_day):
        super().__init__(brand, model, price_per_day)

    def calculate_price(self, days):
        if days <= 0:
            return 0

        return self.price_per_day * days + 50
