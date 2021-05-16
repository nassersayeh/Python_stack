class user:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
class bankaccount (user):
    def __init__(self,firstName,lastName,int_rate, balance):
        super().__init__(firstName, lastName)
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(self.balance,self.int_rate)

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self
    

b = bankaccount("nasser","sayeh",0.01, 30)
a = bankaccount("Mohammad", "Sayeh", 0.02, 20)

b.deposit(10).deposit(10).deposit(10).withdraw(10).yield_interest().display_account_info()
a.deposit(5).deposit(5).withdraw(1).withdraw(1).withdraw(1).withdraw(1).yield_interest().display_account_info()

