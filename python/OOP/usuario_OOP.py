class User:
    #def __init__ para definir atributos de la clase
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # metodo para depositos
    def make_deposit(self, amount): #amount es el argumento del monto del deposito
        self.account_balance += amount #la cuenta del usuario especifico(sefl.) aumenta por la cantidad

    def make_withdrawal (self, amount):
        self.account_balance -= amount

    def display_user_balance (self):
        print ("Usuario:", self.name+",", "Saldo: $" + str( self.account_balance))

    def transfer_money (self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
stev = User("Stev rosaroza", "steve@python.com")

print("--Usuario 1--")

guido.make_deposit(500)#deposito 1
guido.make_deposit(100)#deposito 2
guido.make_deposit(600)#deposito 3
guido.display_user_balance()#saldo 1200
guido.make_withdrawal(200)#retiro 1
guido.display_user_balance()#saldo 1000

print("--Usuario 2--")


monty.make_deposit(120)#deposito 1
monty.make_deposit(180)#deposito 1
monty.make_withdrawal(50)#retiro 1
monty.make_withdrawal(150)#retiro 2
monty.display_user_balance()#saldo 100

print("--Usuario 3--")


stev.make_deposit(600)#deposito 1
stev.make_withdrawal(100)#retiro 1
stev.make_withdrawal(140)#retiro 2
stev.make_withdrawal(160)#retiro 3
stev.display_user_balance()#saldo 200

print("--Transferencia--")

guido.transfer_money(stev,700)
guido.display_user_balance()#saldo 300
stev.display_user_balance()#saldo 900