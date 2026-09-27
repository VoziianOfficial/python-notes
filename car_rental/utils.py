import random
from datetime import datetime


def create_rental_number():
    return random.randint(10000, 99999)

def get_rental_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")