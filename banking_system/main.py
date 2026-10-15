from accounts import BankAccount, DebitAccount, SavingsAccount, CreditAccount
from bank import Bank
from reports import (
    calculate_total_balance,
    count_accounts_by_type,
    find_highest_balance,
)

debit = DebitAccount("Yuliia", 5000, 2000)

savings = SavingsAccount("Anna", 10000, 5000, 2000)

credit = CreditAccount("Alex", 1000, 5000, 3000)


bank = Bank("Python Bank")

print(bank.add_account(debit))
print(bank.add_account(savings))
print(bank.add_account(credit))


print(bank.add_account("Hello"))


print("\n--- ACCOUNTS ---")
bank.show_accounts()


print("\n--- FIND ---")

found = bank.find_account_by_owner("Anna")
print(found.owner)
print(found.balance)

missing = bank.find_account_by_owner("Max")
print(missing)


print("\n--- BANK OPERATIONS ---")

print(bank.withdraw_from_account("Yuliia", 1000))
print(bank.withdraw_from_account("Anna", 3000))
print(bank.withdraw_from_account("Alex", 3500))

print()

bank.show_accounts()


print("\n--- REPORTS ---")

print("Total balance:", calculate_total_balance(bank.accounts))
print("Account types:", count_accounts_by_type(bank.accounts))

highest = find_highest_balance(bank.accounts)

print("Highest balance owner:", highest.owner)
print("Highest balance:", highest.balance)

print("\n--- TRANSFER ---")

print(bank.transfer("Yuliia", "Anna", 1000))

print("Yuliia:", debit.balance)
print("Anna:", savings.balance)
print(bank.transfer("Unknown", "Anna", 500))
