def calculate_total(prices):
    total = 0

    for price in prices:
        total += price

    return total


def apply_discount(total, vip):
    if vip:
        return total * 0.9
    return total
