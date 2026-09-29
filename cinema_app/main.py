from cinema import MovieSession
from utils import create_booking_number, get_booking_date

customer = {"name": "Yuliia", "balance": 1000}


session1 = MovieSession("Avatar", 120, 20)
session2 = MovieSession("Dune", 150, 15)
session3 = MovieSession("Interstellar", 100, 10)

sessions = [session1, session2, session3]


for session in sessions:
    session.show_info()


selected_session = session2
tickets = 3

balance_before = customer["balance"]
seats_before = selected_session.available_seats


if selected_session.book(customer, tickets):
    booking_number = create_booking_number()
    booking_date = get_booking_date()

    print("Booking successful")
    print("Customer:", customer["name"])
    print("Movie:", selected_session.title)
    print("Tickets:", tickets)
    print("Price:", selected_session.calculate_price(tickets))
    print("Booking number:", booking_number)
    print("Date:", booking_date)

    print("Balance before:", balance_before)
    print("Balance after:", customer["balance"])

    print("Seats before:", seats_before)
    print("Seats after:", selected_session.available_seats)

    selected_session.show_info()

    selected_session.cancel_booking(customer, tickets)

    selected_session.show_info()

else:
    print("Booking failed")


print(type(session1))
print(isinstance(session1, MovieSession))
print(vars(session1))
print(hasattr(session1, "title"))
print(getattr(session1, "ticket_price"))
print(MovieSession.__doc__)
