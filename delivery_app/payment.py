def check_payment(balance, order_total):
    if balance >= order_total:
        return True
    else:
        return False



def make_payment(customer, amount):
    if customer["balance"] < amount:
        return False
    else:
        customer["balance"] -= amount
        return True