class user:
    def __init__(self, firstName, lastName, Balance):
        self.firstName = firstName
        self.lastName = lastName
        self.Balance = Balance

    def make_deposit(self, deposit):
        self.Balance += deposit

    def make_withDrow(self, deposit):
        self.Balance -= deposit

    def printBalance(self):
        print(self.Balance)

    def transfer_money(self , x , mone):
        x.make_deposit(mone)
        self.make_withDrow(mone)


x = user("alaa", "ibrahim", 20)
x1 = user("naser", "ibrahim", 30)
x2 = user("lana", "ibrahim", 40)

x.make_deposit(10)
x.make_deposit(20)
x.make_deposit(10)
x.make_withDrow(5)
x.printBalance()
x1.make_deposit(10)
x1.make_deposit(20)
x1.make_withDrow(5)
x1.make_withDrow(10)
x1.printBalance()
x2.make_deposit(10)
x2.make_withDrow(5)
x2.make_withDrow(5)
x2.make_withDrow(10)
x2.printBalance()
x2.transfer_money(x, 20)
x.printBalance()
x2.printBalance()
