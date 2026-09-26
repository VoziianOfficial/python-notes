from booking import calculate_booking, apply_vip_discount, show_hotels
from payment import pay_booking
from utils import create_booking_number, get_booking_date

user = {"name": "Yulia", 
        "balance": 5000, 
        "vip": True}

hotels = [
    {"name": "City Hotel", 
     "price": 1200, "nights": 2},
    {"name": "Sea View", 
     "price": 1700, "nights": 3},
    {"name": "Budget Inn", 
     "price": 700, "nights": 4},
]


show_hotels(hotels)


def find_hotel(hotels, hotel_name):
    for hotel in hotels:
        if hotel["name"] == hotel_name:
            return hotel
    return None


selected_hotel = find_hotel(hotels, "Sea View")


total = calculate_booking(selected_hotel)
final_total = apply_vip_discount(total, user["vip"])
balance_before = user["balance"]

if pay_booking(user, final_total):

    booking_number = create_booking_number()
    booking_date = get_booking_date()

    print("Booking successful")
    print("Customer:", user["name"])
    print("Hotel:", selected_hotel["name"])
    print("Nights:", selected_hotel["nights"])
    print("Price before discount:", total)
    print("Final price:", final_total)
    print("Booking number:", booking_number)
    print("Date:", booking_date)
    print("Balance before:", balance_before)
    print("Balance after:", user["balance"])

else:
    print("Booking failed")
    print("Not enough money")
