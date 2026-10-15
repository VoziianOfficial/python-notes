from accounts import DebitAccount, SavingsAccount, CreditAccount


def calculate_total_balance(accounts):
    total = 0
    for account in accounts:
        total += account.balance

    return total


def count_accounts_by_type(accounts):
    counts = {"debit": 0, "savings": 0, "credit": 0}

    for account in accounts:
        if isinstance(account, DebitAccount):
            counts["debit"] += 1
        elif isinstance(account, SavingsAccount):
            counts["savings"] += 1
        elif isinstance(account, CreditAccount):
            counts["credit"] += 1

    return counts


def find_highest_balance(accounts):
    highest = accounts[0]

    for account in accounts:
        if account.balance > highest.balance:
            highest = account

    return highest
