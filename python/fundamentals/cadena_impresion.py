name = "Zen"
print("Mi nombre es", name)

name = "Zen"
print("Mi nombre es " + name)

num = 45
print("el numero es ", num)

num = 45
#print("el numero es " + num)# cuando la variable es entero no funciona.
print("")


print("# F-Strings (interpolación literal de cadenas)")
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"mi nombre es {first_name} {last_name} y tengo {age} años")




print("# string.format()")

first_name = "Zen"
last_name = "Coder"
age = 27
print("Mi nombre es {} {} y tengo {} años.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("Mi nombre es {} {} y tengo {} años.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.
print("")


print("# % de formato")

hw = "Hola %s" % "mundo" 	# con valores literales
py = "Me encanta Python %d" % 3
print(hw, py)
# salida: Hola mundo Me encanta Python 3
name = "Zen"
age = 27
print("Mi nombre es %s y soy %d" % (name, age))
# o con variables
# Salida: Mi nombre es Zen y tengo 27
print()


print("# Métodos de cadena incorporados")
x = "hola mundo"
print(x.title())
# Salida: "Hola Mundo"... .title() imprime el conteniudo con iniciales en mayusculas
print(x.upper())#salida: HOLA MUNDO


#string.upper(): devuelve una copia de la cadena con todos los caracteres en mayúscula.
#string.lower(): devuelve una copia de la cadena con todos los caracteres en minúsculas.
#string.count(substring): devuelve el número de ocurrencias de subcadena en la cadena.
#string.split(char): devuelve una lista de valores donde la cadena se divide en el carácter dado. Sin un parámetro, la división predeterminada está en cada espacio
#string.find(substring): devuelve el índice del inicio de la primera aparición de subcadena dentro de la cadena.
#string.isalnum(): devuelve booleano dependiendo de si la longitud de la cadena es> 0 y todos los caracteres son alfanuméricos (solo letras y números). Las cadenas que incluyen espacios y signos de puntuación devolverán False para este método. Métodos similares incluyen .isalpha(), .isdigit(), .islower(), .isupper(), y así sucesivamente. Todos regresan booleanos.
#string.join(list):  devuelve una cadena que es todas las cadenas dentro de nuestro conjunto (en este caso, una lista) concatenadas.
#string.endswith(substring): devuelve un valor booleano en función de si los últimos caracteres de la cadena coinciden con la subcadena

lenguajes = ["Go", "Rust", "C", "JavaScript", "PHP", "Python"]
print("Original", lenguajes)

lenguajes.reverse()
print("Reverse: ", lenguajes)#['Python', 'PHP', 'JavaScript', 'C', 'Rust', 'Go']

print(lenguajes[2:])
print(lenguajes[:2])
print(lenguajes[:])
print(lenguajes[::])
print(lenguajes[-2])
print()

invertidos = lenguajes[::-1]
print("Invertidos: ",invertidos)
