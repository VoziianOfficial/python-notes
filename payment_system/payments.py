from utils import generate_transaction_id, get_current_time


class Payment:
    def __init__(self, amount):
        self.amount = amount
        self.transaction_id = generate_transaction_id()
        self.created_at = get_current_time()
        self.status = "pending"

    def show_info(self):
        print(f"Transaction ID: {self.transaction_id}")
        print(f"Amount: {self.amount}")
        print(f"Status: {self.status}")
        print(f"Created at: {self.created_at}")

    def pay(self):
        return False

    def refund(self):
        if self.status == "paid":
            self.status = "refunded"
            return True
        return False


class CardPayment(Payment):
    def __init__(self, amount, card_holder, last_four_digits):
        super().__init__(amount)

        self.card_holder = card_holder
        self.last_four_digits = last_four_digits

    def show_info(self):
        super().show_info()
        print(f"Payment method: Card")
        print(f"Card holder: {self.card_holder}")
        print(f"Card: **** {self.last_four_digits}")


    def pay(self):
        if self.status != "pending":
            return False

        if self.amount <= 0:
            self.status = "failed"
            return False

        self.status = "paid"
        print(f"Card payment of {self.amount} was successful")
        return True


class SwishPayment(Payment):
    def __init__(self, amount, phone_number):
        super().__init__(amount)

        self.phone_number = phone_number

    def show_info(self):
        super().show_info()
        print(f"Payment method: Swish")
        print(f"Phone number: {self.phone_number}")

    def pay(self):
        if self.status != "pending":
            return False

        if self.amount <= 0:
            self.status = "failed"
            return False

        self.status = "paid"
        print(f"Swish payment of {self.amount} was successful")
        return True


class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)

        self.email = email

    def show_info(self):
        super().show_info()
        print(f"Payment method: PayPal")
        print(f"Email: {self.email}")


    def pay(self):
        if self.status != "pending":
            return False

        if self.amount <= 0:
            self.status = "failed"
            return False

        self.status = "paid"
        print(f"PayPal payment of {self.amount} was successful")
        return True
