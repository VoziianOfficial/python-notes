import random
from datetime import datetime 


def create_order_number():
    """Creates a random order number."""
    return random.randint(1000, 9999)


def get_order_date():
    """Returns the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")