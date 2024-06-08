class BankAccount:
    def __init__(self, account_number: str, account_holder: str, balance: float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        return self.balance

# Example usage
account = BankAccount("123456789", "John Doe", 100.0)
print(account.get_balance())

account.deposit(50.0)
print(account.get_balance())

successful_withdrawal = account.withdraw(70.0)
print(successful_withdrawal)
print(account.get_balance())

unsuccessful_withdrawal = account.withdraw(100.0)
print(unsuccessful_withdrawal)
print(account.get_balance())
