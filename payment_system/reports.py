from payments import CardPayment, SwishPayment, PayPalPayment

def calculate_paid_total(orders):
    total = 0

    for order in orders:
        if order.status == "paid":
            total += order.payment.amount
    return total 

def count_orders_by_status(orders):
    counts = {"created": 0, "paid": 0, "refunded": 0}

    for order in orders:
        counts[order.status] += 1

    return counts


def count_payment_types(orders):
    counts = {"card": 0, "swish": 0, "paypal": 0}

    for order in orders:
        if isinstance(order.payment, CardPayment):
            counts["card"] += 1

        elif isinstance(order.payment, SwishPayment):
            counts["swish"] += 1

        elif isinstance(order.payment, PayPalPayment):
            counts["paypal"] += 1

    return counts
