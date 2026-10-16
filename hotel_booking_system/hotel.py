from rooms import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.bookings = []

    def add_room(self, room):
        if isinstance(room, Room):
            self.rooms.append(room)
            return True
        else:
            return False

    def find_room_by_number(self,room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room

        return None

    def show_available_rooms(self):
        for room in self.rooms:
            if room.available:
                print(f"Room number: {room.room_number}, Type: {room.__class__.__name__}, Price per night: {room.price_per_night}")

    def add_booking(self, booking):
        result = booking.confirm()

        if result == False:
            return False

        self.bookings.append(booking)
        return True
