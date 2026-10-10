from utils import generate_delivery_id, get_current_time


class Delivery:
    """
    Base class for delivery types.
    """

    def __init__(self, customer_name, address, distance):
        self.customer_name = customer_name
        self.address = address
        self.distance = distance

        self.delivery_id = generate_delivery_id()
        self.status = "created"
        self.created_at = get_current_time()

    def show_info(self):
        print(f"Delivery ID: {self.delivery_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Address: {self.address}")
        print(f"Distance: {self.distance}")
        print(f"Status: {self.status}")
        print(f"Created at: {self.created_at}")

    def calculate_price(self):
        return 0

    def deliver(self):
        print("Delivery is in progress")

    def complete(self):
        if self.status == "completed":
            return False
        self.status = "completed"
        return True


class CourierDelivery(Delivery):
    def __init__(self, courier_name, customer_name, address, distance):
        super().__init__(customer_name, address, distance)
        self.courier_name = courier_name

    def calculate_price(self):
        return 50 + self.distance * 10

    def deliver(self):
        print(f"{self.courier_name} is delivering the order to {self.customer_name}")

    def show_info(self):
        super().show_info()
        print(f"Courier Name: {self.courier_name}")


class CarDelivery(Delivery):
    def __init__(self, driver_name, car_number, customer_name, address, distance):
        super().__init__(customer_name, address, distance)
        self.driver_name = driver_name
        self.car_number = car_number

    def calculate_price(self):
        return 100 + self.distance * 8

    def deliver(self):
        print(
            f"Driver {self.driver_name} is delivering the order by car {self.car_number}"
        )

    def show_info(self):
        super().show_info()
        print(f"Driver Name: {self.driver_name}")
        print(f"Car Number: {self.car_number}")


class PickupDelivery(Delivery):
    def __init__(self, pickup_point, customer_name, address, distance):
        super().__init__(customer_name, address, distance)
        self.pickup_point = pickup_point

    def calculate_price(self):
        return 0

    def deliver(self):
        print(f"{self.customer_name} will pick up the order from {self.pickup_point}.")

    def show_info(self):
        super().show_info()
        print(f"Pickup Point: {self.pickup_point}")
