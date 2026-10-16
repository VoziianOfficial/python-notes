from rooms import StandardRoom, DeluxeRoom, FamilyRoom
from booking import Booking
from hotel import Hotel
from reports import (
    calculate_confirmed_revenue,
    count_rooms_by_type,
    count_bookings_by_status,
)

standard = StandardRoom(101, 800)
deluxe = DeluxeRoom(201, 1200)
family = FamilyRoom(301, 1000)


rooms = [standard, deluxe, family]


for room in rooms:
    print(room.__class__.__name__)
    print("3 nights:", room.calculate_price(3))
    print()


print(standard.price_per_night)

standard.price_per_night = 900
print(standard.price_per_night)

standard.price_per_night = -500
print(standard.price_per_night)


print(standard.available)

print(standard.reserve())
print(standard.available)

print(standard.reserve())

print(standard.release())
print(standard.available)


room1 = StandardRoom(102, 800)

booking = Booking("Yuliia", room1, 3)

print("Total:", booking.calculate_total())

print("Confirm:", booking.confirm())
print("Booking:", booking.status)
print("Room available:", room1.available)

print("Second confirm:", booking.confirm())

print("Cancel:", booking.cancel())
print("Booking:", booking.status)
print("Room available:", room1.available)

print("Second cancel:", booking.cancel())


hotel = Hotel("Sea View Hotel")

print(hotel.add_room(standard))
print(hotel.add_room(deluxe))
print(hotel.add_room(family))

print("\n--- FIND ROOM ---")
found_room = hotel.find_room_by_number(201)

if found_room:
    print(found_room.room_number)
    print(found_room.__class__.__name__)

print("\n--- AVAILABLE ROOMS ---")
hotel.show_available_rooms()


room2 = StandardRoom(103, 700)
hotel.add_room(room2)

booking2 = Booking("Anna", room2, 2)

print("\n--- HOTEL BOOKING ---")
print(hotel.add_booking(booking2))
print("Status:", booking2.status)
print("Available:", room2.available)
print("Bookings:", len(hotel.bookings))


booking3 = Booking("Alex", deluxe, 2)
print("\nAdd Alex booking:", hotel.add_booking(booking3))

booking4 = Booking("Maria", deluxe, 1)
print("Add Maria booking:", hotel.add_booking(booking4))

booking2.cancel()

all_bookings = [booking2, booking3, booking4]


print("\n--- REPORTS ---")

print("Confirmed revenue:", calculate_confirmed_revenue(all_bookings))

print("Room types:", count_rooms_by_type(hotel.rooms))

print("Booking statuses:", count_bookings_by_status(all_bookings))
