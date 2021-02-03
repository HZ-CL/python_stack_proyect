class User:
    #def __init__ para definir atributos de la clase
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # metodo para depositos
    def make_deposit(self, amount): #amount es el argumento del monto del deposito
        self.account_balance += amount #la cuenta del usuario especifico(sefl.) aumenta por la cantidad
        return self

    def make_withdrawal (self, amount):
        self.account_balance -= amount
        return self


    def display_user_balance (self):
        print ("Usuario: " + self.name + "," , "Saldo: $" + str( self.account_balance))
        return self


    def transfer_money (self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self



guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
stev = User("Stev rosaroza", "steve@python.com")

print("--Usuario 1--")
guido.make_deposit(500).make_deposit(100).make_deposit(600).display_user_balance().make_withdrawal(200).display_user_balance()

print()
print("--Usuario 2--")
monty.make_deposit(120).make_deposit(180).make_withdrawal(50).make_withdrawal(150).display_user_balance()

print()
print("--Usuario 3--")
stev.make_deposit(600).make_withdrawal(100).make_withdrawal(140).make_withdrawal(160).display_user_balance()

print()
print("--Transferencia--")
guido.transfer_money(stev,700).display_user_balance()
stev.display_user_balance()