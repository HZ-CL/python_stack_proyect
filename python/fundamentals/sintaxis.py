# def (funciones)
# if, elif, else(Sentencias condicionales)
# for, while(bucles)
#Class clases:
#    pass PARA DECIRLE A LA CONSOLA QUE PASE DE LA EJECUCION DEL CODIGO



print("# Tipos de Datos Primitivos")

print("Valores booleanos")#True y False, Verdadero y falso, siempre con T y F en mayusculas.
is_hungry = True
has_freckles = False
print()


print("Numeros")#numeros enteros, con coma flotanate(decimales) y numeros complejos
age = 35 # storing an int
weight = 160.57 # storing a float
print()


print("Cadenas")
name = "Hector Zambrano"
print()




print("# Tipos Compuestos")


print("Tuplas")#un tipo de datos que es inmutable (no se puede modificar después de su creación) y puede contener un grupo de valores.
# Las tuplas pueden contener tipos de datos mixtos.
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# output: Bruce
dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)
print()

print("Listas")#un tipo de datos que es mutable y puede contener un grupo de valores.
# Generalmente destinado a almacenar una colección de datos relacionados.
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']
print()


print("Diccionarios")


my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# salida: 0 abc, 1 123, 2 xyz
# OR
for v in my_list:
    print(v)
# salida: abc, 123, xyz
