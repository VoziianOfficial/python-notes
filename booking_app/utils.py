import random
from datetime import datetime


def create_booking_number():
    return random.randint(100000, 999999)

def get_booking_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
