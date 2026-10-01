class Order:
    """
    Represents a customer order.
    """

    def __init__(self, customer, items, status, order_number, order_date):
        self.customer = customer
        self.items = items
        self.status = status
        self.order_number = order_number
        self.order_date = order_date

    def add_product(self, product, quantity):
        if quantity <= 0:
            return False

        if self.status != "new":
            return False

        if not product.is_available(quantity):
            return False

        self.items.append({"product": product, "quantity": quantity})

        return True

    def calculate_total(self):
        total = 0

        for item in self.items:
            total += item["product"].price * item["quantity"]

        return total

    def show_items(self):
        for number, item in enumerate(self.items, start=1):
            subtotal = item["product"].price * item["quantity"]

            print(f"{number}. Product: {item['product'].name}")
            print(f"Quantity: {item['quantity']}")
            print(f"Price: {item['product'].price}")
            print(f"Subtotal: {subtotal}")

    def checkout(self):
        if self.status != "new":
            return False

        if self.items == []:
            return False

        for item in self.items:
            if not item["product"].is_available(item["quantity"]):
                return False

        total = self.calculate_total()

        if not self.customer.pay(total):
            return False

        for item in self.items:
            item["product"].reduce_stock(item["quantity"])

        self.status = "paid"

        return True

    def cancel(self):
        if self.status != "paid":
            return False

        total = self.calculate_total()

        self.customer.refund(total)

        for item in self.items:
            item["product"].restore_stock(item["quantity"])

        self.status = "cancelled"

        return True
