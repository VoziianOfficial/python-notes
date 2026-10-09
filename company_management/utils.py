import random
from datetime import datetime


def generate_employee_id():
    """
    Generates a random employee ID.
    """
    return random.randint(1000, 9999)



def get_current_time():
    """
    Returns the current date and time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
