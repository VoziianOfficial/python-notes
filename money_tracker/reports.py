def calculate_balance(transactions):
    balance = 0

    for transaction in transactions:
        if transaction["type"] == "income":
            balance += transaction["amount"]
        elif transaction["type"] == "expense":
            balance -= transaction["amount"]
    return balance





def calculate_expenses(transactions):
    total = 0
    for transaction in transactions:
        if transaction["type"] == "expense":
            total += transaction["amount"]
    return total


def category_expenses(transactions, category):
    total = 0
    for transaction in transactions:
        if transaction["type"] == "expense" and transaction["category"] == category:
            total += transaction["amount"]
    return total