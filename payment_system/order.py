class Order:
    def __init__(self, customer_name, items, payment):
        self.customer_name = customer_name
        self.items = items
        self.payment = payment
        self.status = "created"

    def show_order(self):
        print(f"Customer Name: {self.customer_name}")
        print("Items:")
        for item in self.items:
            print(f"- {item}")
        print(f"Payment method: {self.payment.__class__.__name__}")
        print(f"Amount: {self.payment.amount}")
        print(f"Order status: {self.status}")

    def pay_order(self):
        if self.status == "paid":
            return False

        result = self.payment.pay()

        if result:
            self.status = "paid"
            return True

        return False

    def refund_order(self):
        if self.status != "paid":
            return False

        result = self.payment.refund()

        if result:
            self.status = "refunded"
            return True

        return False
