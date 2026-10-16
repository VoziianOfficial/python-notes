class Booking:
    def __init__(self, guest_name, room, nights):
        self.guest_name = guest_name
        self.room = room
        self.nights = nights
        self.status = "created"

    def calculate_total(self):
        return self.room.calculate_price(self.nights)

    def confirm(self):
        if self.status != "created":
            return False

        if self.nights <= 0:
            return False

        if self.room.available == False:
            return False

        result = self.room.reserve()

        if result == False:
            return False

        self.status = "confirmed"
        return True

    def cancel(self):
        if self.status != "confirmed":
            return False

        result = self.room.release()

        if result == False:
            return False

        self.status = "cancelled"
        return True