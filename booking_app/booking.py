def calculate_booking(hotel):
    return hotel["price"] * hotel["nights"]


def apply_vip_discount(total, vip):
    if vip == True:
        return total * 0.85
    return total


def show_hotels(hotels):
    for hotel in hotels:
        print(f"{hotel['name']} - ${hotel['price']} per night for {hotel['nights']} nights")
