from bank_account import BankAccount


account = BankAccount("Yuliia", 1000)

print(account.balance)

account.deposit(500)
account.withdraw(200)


account.__balance = 999999

print("account.__balance:", account.__balance)
print("account.balance:", account.balance)


print("Start:", account.balance)

account.deposit(500)
print("After deposit:", account.balance)

account.withdraw(200)
print("After withdraw:", account.balance)
