class Order:
    """
    Represents a food delivery order.
    """
    def __init__(self, customer_name, products, balance):
        self.customer_name = customer_name
        self.products = products
        self.balance = balance

    def show_products(self):
        """
        Displays all products in the order.
        """

        for product in self.products:
            print(f"Product: {product['name']}, Price: {product['price']}")

    def calculate_total(self):
        total = 0

        for product in self.products:
            total += product['price']
            self.total = total
        return total

    def calculate_final_price(self):
        """
        Calculates the order price including delivery.
        """
        total = self.calculate_total()

        if total > 500:
            return total
        else:
            return total + 50

    def pay(self):
        final_price = self.calculate_final_price()
        if self.balance < final_price:
            print("Insufficient balance to complete the order.")
            return False
        else: 
            self.balance -= final_price
            print(f"Payment successful! Remaining balance: {self.balance}")
            return True
