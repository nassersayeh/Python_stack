class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount

        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance+(self.balance*self.int_rate)
        return self


class user():
    def __init__(self, int_rate, balance, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account = BankAccount(int_rate, balance)



x = user(2, 100, "nasser", "sayeh")
x.account.display_account_info(
).deposit(100).display_account_info().withdraw(100)
