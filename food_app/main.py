from order import Order
from utils import create_order_number, get_order_date


products = [
    {"name": "Pizza", "price": 120},
    {"name": "Burger", "price": 90},
    {"name": "Coffee", "price": 40},
]

order = Order("Yuliia", products, 1000)

order.show_products()

total = order.calculate_total()
print(f"Total price of the order: {total}")

final_price = order.calculate_final_price()
print(f"Final price including delivery: {final_price}")

balance_before = order.balance

if order.pay():
    order_number = create_order_number()
    order_date = get_order_date()

    print("Customer:", order.customer_name)
    print("Order number:", order_number)
    print("Final price:", final_price)
    print("Balance before:", balance_before)
    print("Balance after:", order.balance)
    print("Order date:", order_date)

else:
    print("Payment failed")
