class User:
    #def __init__ para definir atributos de la clase
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
# metodo para depositos
    def make_deposit(self, amount): #amount es el argumento del monto del deposito
        self.account.deposit(amount) #la cuenta del usuario especifico(sefl.) aumenta por la cantidad
        return self

    def make_withdrawal (self, amount):
        self.account.withdraw(amount)
        return self


    def display_user_balance (self):
        print("Nombre:",self.name+",", "saldo: $ "+str(self.account.balance))
        #print ("Usuario: " + self.name + "," , "Saldo: $" + str( self.account_balance))
        return self


    def transfer_money (self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self



class BankAccount:
    def __init__(self, int_rate, balance):
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

    #def display_account_info(self):
        #self.balance
        #print(self.balance)
        #print("Saldo: $"+str(self.balance))
        #return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self


guido = User("Guido Van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
stev = User("Stev Rosaroza", "steve@python.com")

guido.make_deposit(100).make_withdrawal(50).transfer_money(monty,30).display_user_balance().make_deposit(20).display_user_balance()