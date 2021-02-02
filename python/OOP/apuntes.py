

#Creacion de una clase "user"

class User:
    #def __init__ para definir atributos de la clase
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # metodo para depositos
    def make_deposit(self, amount): #amount es el argumento del monto del deposito
        self.account_balance += amount #la cuenta del usuario especifico(sefl.) aumenta por la cantidad

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

print("--Datos de usuario  --")
print(guido.name) #Output: Guido van Rossum
print("--                  --")

print("--Llamado al metodo para depositos--")
guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50
print("--        --")
