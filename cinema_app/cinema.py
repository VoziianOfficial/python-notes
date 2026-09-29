class MovieSession:
    """
    Represents a movie session in a cinema.
    """

    def __init__(self, title, ticket_price, available_seats):
        self.title = title
        self.ticket_price = ticket_price
        self.available_seats = available_seats

    def show_info(self):
        print(f"Movie: {self.title}")
        print(f"Ticket price: {self.ticket_price}")
        print(f"Available seats: {self.available_seats}")

    def calculate_price(self, tickets):
        total = self.ticket_price * tickets
        return total

    def book(self, customer, tickets):
        if self.available_seats < tickets:
            print("Not enough available seats.")
            return False

        total = self.calculate_price(tickets)

        if customer["balance"] < total:
            return False

        customer["balance"] -= total
        self.available_seats -= tickets
        return True

    def cancel_booking(self, customer, tickets):
        refund = self.calculate_price(tickets)
        customer["balance"] += refund
        self.available_seats += tickets
