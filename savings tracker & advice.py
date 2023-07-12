class SavingsTracker:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} made. Current balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} made. Current balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

    def advice(self):
        if self.balance == 0:
            print("Your savings balance is currently empty. Start saving now!")
        elif self.balance < 1000:
            print("You have a small amount of savings. Consider saving more.")
        elif self.balance < 5000:
            print("Your savings are growing steadily. Keep it up!")
        else:
            print("Congratulations! You have a healthy savings balance.")

# Example usage
tracker = SavingsTracker()
tracker.deposit(1000)
tracker.withdraw(200)
tracker.advice()
