
class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
		# your code here! (remember, this is where we specify the attributes for our class)
        # # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        withdraw_cost = 5
        if self.balance - (amount + withdraw_cost) < 0:
            print("Fondos insuficientes: se cobrar una tarifa de $ 5")
            self.balance -= withdraw_cost
        else:
            self.balance -= amount+withdraw_cost
        return self

    def display_account_info(self):
        print("Saldo: $"+str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

guido = BankAccount()
monty = BankAccount(balance=100)
stev = BankAccount()

print("--Cuenta 1--")
guido.deposit(100).deposit(80).deposit(50).withdraw(25).yield_interest().display_account_info()
print()
print("--Cuenta 2--")
monty.deposit(3000).deposit(200).withdraw(2200).withdraw(390).withdraw(100).withdraw(600).display_account_info().yield_interest().display_account_info()
