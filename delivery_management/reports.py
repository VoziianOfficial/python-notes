from deliveries import CourierDelivery, CarDelivery, PickupDelivery


def calculate_total_delivery_income(orders):
    total = 0

    for order in orders:
        total += order.delivery.calculate_price()
    return total


def count_delivery_types(orders):
    counts = {"courier": 0, "car": 0, "pickup": 0}

    for order in orders:
        if isinstance(order.delivery, CourierDelivery):
            counts["courier"] += 1

        elif isinstance(order.delivery, CarDelivery):
            counts["car"] += 1

        elif isinstance(order.delivery, PickupDelivery):
            counts["pickup"] += 1

    return counts
