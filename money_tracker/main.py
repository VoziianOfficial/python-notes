from transactions import add_transaction
from reports import calculate_balance, calculate_expenses, category_expenses

transactions = [
    {"category": "Salary", "amount": 15000, "type": "income"},
    {"category": "Food", "amount": 800, "type": "expense"},
    {"category": "Transport", "amount": 300, "type": "expense"},
    {"category": "Freelance", "amount": 5000, "type": "income"},
    {"category": "Food", "amount": 1200, "type": "expense"},
]

add_transaction(transactions, "Shopping", 1500, "expense")


balance = calculate_balance(transactions)
expenses = calculate_expenses(transactions)
food = category_expenses(transactions, "Food")

print("Balance:", balance)
print("All expenses:", expenses)
print("Food expenses:", food)
