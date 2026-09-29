import random
from datetime import datetime


def create_booking_number():
    """
    Creates a random cinema booking number.
    """
    return random.randint(1000, 9999)


def get_booking_date():
    """
    Returns the current date and time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")