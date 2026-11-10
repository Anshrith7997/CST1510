class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance:
            print("Not enough money!")
        else:
            self.balance -= amount

    def show_balance(self):
        print(self.owner, "balance: £", self.balance)
