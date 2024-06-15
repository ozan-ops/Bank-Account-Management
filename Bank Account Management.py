class Account:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    # Print method
    def __str__(self):
        return f"Account holder: {self.name}\nAccount balance: {self.balance}"

    # Deposit method
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)


acct1 = Account('Jose', 100)
print(acct1)
print(acct1.name)
print(acct1.balance)

acct1.deposit(50)
