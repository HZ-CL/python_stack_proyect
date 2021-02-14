# 1 Actualiza los valores en diccionarios y listas

# a.- Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
x = [ [5,2,3], [10,8,9] ]

print(x)
print(x[1][0])
x[1][0] = 15
print(x[1])

# b.- Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

print(students[0]['last_name'])
students[0]['last_name'] = 'Bryant'
print(students[0])


# c.- En el directorio sports_directory, cambia 'Messi' a 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

print(sports_directory['soccer'][0])
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

# d.- Camba el valor 20 en z a 30
z = [ {'x': 10, 'y': 20} ]

print(z[0]['y'])
z[0]['y'] = 30
print(z)


# 2 Itera a través de una lista de diccionarios
#  Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios, la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado. Por ejemplo, dada la siguiente lista:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
# La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
# Bonus: Hacer que aparezcan exactamente así!
    #for fl in some_list:
        #print(fl)
    for key, val in some_list:
        print(key," = ",val)

x = iterateDictionary(students)
print(x)


# 3 Obtén valores de una lista de diccionarios
#  Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
print(students[0]['last_name']+' '+students[0]['first_name'])

def iterateDictionary2(key_name, some_list):
    for key in range(0, len(some_list)):
        if key_name == 'frist_name':
            #print(key) #para ver el valor de key
            print(key)
            #print(some_list[key]['first_name'])
        if key_name == 'last_name':
            #print(key)
            print(some_list[key]['last_name'])
h=iterateDictionary2('frist_name', students)



# 4 Itera a través de un diccionario con valores de listas
# Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for i in dict:
        #print(i) #control para saber el valor de i
        print(len(dict[i]), i)
        for a in range(len(dict[i])):
            print(dict[i][a])
        print()


print(printInfo(dojo))




def bubbleSort(arr): 
    n = len(arr)

    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),