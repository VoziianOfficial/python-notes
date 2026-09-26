def pay_booking(user, amount):
    if user["balance"] < amount:
        return False
    elif user["balance"] >= amount:
        user["balance"] -= amount
        return True