from deliveries import Delivery, PickupDelivery, CourierDelivery, CarDelivery
from order import Order
from service import DeliveryService
from reports import calculate_total_delivery_income, count_delivery_types

courier_delivery = CourierDelivery("Oleg", "Yuliia", "Karlskrona", 4)

car_delivery = CarDelivery("Max", "ABC123", "Masha", "Ronneby", 15)

pickup_delivery = PickupDelivery(
    "Karlskrona Central Pickup Point", "Alex", "Karlskrona", 0
)


order1 = Order(
    "Yuliia",
    [{"product": "Pizza", "quantity": 2}, {"product": "Burger", "quantity": 1}],
    courier_delivery,
)

order2 = Order(
    "Masha",
    [{"product": "Coffee", "quantity": 3}, {"product": "Juice", "quantity": 2}],
    car_delivery,
)

order3 = Order(
    "Alex",
    [{"product": "Cake", "quantity": 1}, {"product": "Ice Cream", "quantity": 2}],
    pickup_delivery,
)


orders = [order1, order2, order3]


service = DeliveryService()

service.add_order(order1)
service.add_order(order2)
service.add_order(order3)


print("\n--- DELIVERY SERVICE ---")

service.show_orders()
service.process_orders()


print("\n--- COMPLETE DELIVERY ---")

print(courier_delivery.status)

print(courier_delivery.complete())
print(courier_delivery.status)

print(courier_delivery.complete())
print(courier_delivery.status)


print("\n--- REPORTS ---")

print("Total delivery income:", calculate_total_delivery_income(orders))
print("Delivery types:", count_delivery_types(orders))
