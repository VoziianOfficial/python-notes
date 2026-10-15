from accounts import BankAccount


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        if not isinstance(account, BankAccount):
            return False
        else:
            self.accounts.append(account)
            return True

    def find_account_by_owner(self, owner):
        for account in self.accounts:
            if account.owner == owner:
                return account

        return None

    def show_accounts(self):
        for account in self.accounts:
            print(f"Owner: {account.owner}")
            print(f"Type: {account.__class__.__name__}")
            print(f"Balance: {account.balance}")
            print()

    def withdraw_from_account(self, owner, amount):
        account = self.find_account_by_owner(owner)

        if account is None:
            return False

        return account.withdraw(amount)

    def deposit_to_account(self, owner, amount):
        account = self.find_account_by_owner(owner)

        if account is None:
            return False

        return account.deposit(amount)

    def transfer(self, from_owner, to_owner, amount):
        from_account = self.find_account_by_owner(from_owner)
        to_account = self.find_account_by_owner(to_owner)

        if from_account is None or to_account is None:
            return False

        result = from_account.withdraw(amount)
        

        if result == False:
            return False

        to_account.deposit(amount)
        return True

