def calculate_order(products):
    total = 0
    for product in products:
        total += product["price"]
    return total


def apply_delivery(total):
    if total > 500:
        return total 
    else:
        return total + 50


def show_products(products):
    for product in products:
        print(product["name"], "-", product["price"])
