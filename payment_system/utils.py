import random 
from datetime import datetime


def generate_transaction_id():
    return f"TRX-{random.randint(1000, 9999)}"




def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")