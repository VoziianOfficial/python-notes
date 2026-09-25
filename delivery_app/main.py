from orders import calculate_order, apply_delivery, show_products
from payment import  make_payment
from delivery import get_delivery_status

import random
from datetime import datetime


customer = {
    "name": "Yulia", 
    "balance": 1000, 
    "distance": 7
    }


products = [
    {"name": "Pizza", "price": 120},
    {"name": "Burger", "price": 90},
    {"name": "Coffee", "price": 40},
]


total = calculate_order(products)
final_total = apply_delivery(total)
delivery_status = get_delivery_status(customer["distance"])

balance_before = customer["balance"]

if make_payment(customer, final_total):
    order_number = random.randint(1000, 9999)
    order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("Order successful")
    print("Customer:", customer["name"])
    print("Order number:", order_number)
    print("Products total:", total)
    print("Final total:", final_total)
    print("Delivery:", delivery_status)
    print("Date:", order_date)

    print("Balance before:", balance_before)
    print("Order:", final_total)
    print("Balance after:", customer["balance"])

    show_products(products)

else:
    print("Payment failed")
