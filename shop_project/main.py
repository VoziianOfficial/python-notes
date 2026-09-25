from orders import calculate_total, apply_discount
from payment import check_payment

import random
from datetime import datetime


username = "Julia"
balance = 5000
vip = True

prices = [500, 1200, 300]


total = calculate_total(prices)
final_price = apply_discount(total, vip)

print("Total:", total)
print("Final price:", final_price)

if check_payment(balance, final_price):
    print("Payment successful")

    order_number = random.randint(1000, 9999)
    order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("Order number:", order_number)
    print("Order date:", order_date)

else:
    print("Not enough money")
