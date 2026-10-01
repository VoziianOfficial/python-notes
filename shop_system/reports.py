def show_inventory(products):
    for product in products:
        product.show_info()


def calculate_inventory_value(products):
    total = 0
    for product in products:
        total += product.price * product.stock
    return total


def find_product(products, product_name):
    for product in products:
        if product.name == product_name:
            return product

    return None
