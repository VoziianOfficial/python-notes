class Order:
    def __init__(self, customer_name, items, delivery):
        self.customer_name = customer_name
        self.items = items
        self.delivery = delivery

    def show_order(self):
        print(f"Customer Name: {self.customer_name}")
        print("Items:")

        for item in self.items:
            print(f"- {item['product']} x {item['quantity']}")

        print(f"Delivery type: {self.delivery.__class__.__name__}")
        print(f"Delivery price: {self.delivery.calculate_price()}")

    def send_order(self):
        self.delivery.deliver()
