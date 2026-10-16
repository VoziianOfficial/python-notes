from rooms import StandardRoom, DeluxeRoom, FamilyRoom


def calculate_confirmed_revenue(bookings):
    total_revenue = 0

    for booking in bookings:
        if booking.status == "confirmed":
            total_revenue += booking.calculate_total()

    return total_revenue


def count_rooms_by_type(rooms):
    counts = {"standard": 0, "deluxe": 0, "family": 0}

    for room in rooms:
        if isinstance(room, StandardRoom):
            counts["standard"] += 1

        if isinstance(room, DeluxeRoom):
            counts["deluxe"] += 1

        if isinstance(room, FamilyRoom):
            counts["family"] += 1

    return counts


def count_bookings_by_status(bookings):
    counts = {"created": 0, "confirmed": 0, "cancelled": 0}

    for booking in bookings:
        if booking.status == "created":
            counts["created"] += 1

        if booking.status == "confirmed":
            counts["confirmed"] += 1

        if booking.status == "cancelled":
            counts["cancelled"] += 1

    return counts
