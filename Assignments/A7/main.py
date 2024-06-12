class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def check_balance(self):
        return self.__balance

    def account_details(self):
        return f"Account Number: {self.__account_number}\nAccount Holder: {self.__account_holder}\nBalance: {self.__balance}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.01):
        super().__init__(account_number, account_holder, balance)
        self.__interest_rate = interest_rate

    def apply_interest(self):
        interest = self.check_balance() * self.__interest_rate
        self.deposit(interest)

    def account_details(self):
        details = super().account_details()
        return f"{details}\nInterest Rate: {self.__interest_rate * 100}%"
    
class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=100.0):
        super().__init__(account_number, account_holder, balance)
        self.__overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.check_balance() + self.__overdraft_limit:
            new_balance = self.check_balance() - amount
            if new_balance < 0:
                self.__overdraft_limit += new_balance
                new_balance = 0
            self._BankAccount__balance = new_balance
        else:
            print("Overdraft limit exceeded!")

    def account_details(self):
        details = super().account_details()
        return f"{details}\nOverdraft Limit: {self.__overdraft_limit}"

# Create a Savings Account
savings = SavingsAccount("SA123", "John Doe", 1000.0)
savings.deposit(500)
savings.apply_interest()
print(savings.account_details())
print("Balance after interest:", savings.check_balance())

# Create a Checking Account
checking = CheckingAccount("CA123", "Jane Doe", 500.0)
checking.deposit(200)
checking.withdraw(600)
print(checking.account_details())
print("Balance after withdrawal:", checking.check_balance())
