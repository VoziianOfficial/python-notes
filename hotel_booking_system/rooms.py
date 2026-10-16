from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self, room_number, price_per_night):
        self.room_number = room_number
        self.__price_per_night = price_per_night
        self.__available = True

    @property
    def price_per_night(self):
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, value):
        if value <= 0:
            return

        self.__price_per_night = value

    @property
    def available(self):
        return self.__available

    def reserve(self):
        if not self.available:
            return False

        self.__available = False
        return True

    def release(self):
        if self.available:
            return False

        self.__available = True
        return True

    @abstractmethod
    def calculate_price(self, nights):
        pass


class StandardRoom(Room):
    def __init__(self, room_number, price_per_night):
        super().__init__(room_number, price_per_night)

    def calculate_price(self, nights):
        if nights <= 0:
            return 0

        return self.price_per_night * nights


class DeluxeRoom(Room):
    def __init__(self, room_number, price_per_night):
        super().__init__(room_number, price_per_night)

    def calculate_price(self, nights):
        if nights <= 0:
            return 0

        total = self.price_per_night * nights
        return total + total * 0.15


class FamilyRoom(Room):
    def __init__(self, room_number, price_per_night):
        super().__init__(room_number, price_per_night)
        self.cleaning_fee = 300

    def calculate_price(self, nights):
        if nights <= 0:
            return 0

        total = self.price_per_night * nights
        return total + self.cleaning_fee
