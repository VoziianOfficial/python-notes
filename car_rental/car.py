class Car:
    """
    Represents a rental car.
    """

    def __init__(self, brand, model, price_per_day):

        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day
        self.available = True

    def show_info(self):
        if self.available:
            status = "Available"
        else:
            status = "Not available"

        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price per day: {self.price_per_day}")
        print(f"Status: {status}")

    def calculate_price(self, days):

        return self.price_per_day * days

    def rent(self, customer, days):
        if not self.available:
            print(f"Sorry, the car {self.brand} {self.model} is not available for rent.")
            return False

        total = self.calculate_price(days)
        if customer["balance"] < total:
            print(f"Sorry, {customer['name']} does not have enough balance to rent the car.")
            return False
        else:
            customer["balance"] -= total
            self.available = False
            return True

    def return_car(self):
        self.available = True

