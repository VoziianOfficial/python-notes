import random
from datetime import datetime


def add_transaction(transactions, category, amount, type):
    transactions.append({
        "category": category, 
        "amount": amount, 
        "type": type})



operation_id = random.randint(1000, 9999)
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
