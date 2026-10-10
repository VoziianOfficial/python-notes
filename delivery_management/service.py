class DeliveryService:
    def __init__(self):
        self.orders = []


    def add_order(self, order):
        self.orders.append(order)


    def show_orders(self):
        for order in self.orders:
            order.show_order()


    def process_orders(self):
        for order in self.orders:
            order.send_order()