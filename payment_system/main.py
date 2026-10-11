from payments import Payment, CardPayment, PayPalPayment, SwishPayment
from order import Order
from reports import calculate_paid_total, count_orders_by_status, count_payment_types

card_order_payment = CardPayment(1500, "Yuliia", "4821")

swish_order_payment = SwishPayment(700, "+46701234567")

paypal_order_payment = PayPalPayment(1200, "alex@example.com")


order1 = Order("Yuliia", ["Laptop", "Mouse"], card_order_payment)

order2 = Order("Anna", ["Headphones"], swish_order_payment)

order3 = Order("Alex", ["Keyboard", "Monitor"], paypal_order_payment)


print("\n--- ORDER TEST ---")

order1.show_order()

print("Pay result:", order1.pay_order())
print("Order status:", order1.status)
print("Payment status:", order1.payment.status)

print("Second pay:", order1.pay_order())

print("Refund:", order1.refund_order())
print("Order status:", order1.status)
print("Payment status:", order1.payment.status)

print("Second refund:", order1.refund_order())


print("\n--- POLYMORPHISM ---")

orders = [order2, order3]

for order in orders:
    order.show_order()
    print("Payment result:", order.pay_order())
    print()


print("\n--- REPORTS ---")

all_orders = [order1, order2, order3]

print("Paid total:", calculate_paid_total(all_orders))
print("Orders by status:", count_orders_by_status(all_orders))
print("Payment types:", count_payment_types(all_orders))
