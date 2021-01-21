# 1 Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
# Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]


def elbig(lista):
    for x in range(0, len(lista)):
        if lista[x] > 0:
            lista[x] = "big"
    return lista

m = elbig([1, -3, -5, 5])
print(m)


# 2 Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
# Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
# Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve

def positivos(arreglo):
    cuenta = 0
    for x in arreglo:
        if x > 0:
            cuenta = cuenta + 1
    arreglo[-1] = cuenta
    return arreglo
a = positivos([1,6, -4, -2, -7, -2])
print(a)


# 3 Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
# Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
# Ejemplo: sum_total ([6,3, -2]) debería devolver 7

def suma_total(sumar):
    sumador = 0
    for x in sumar:
        sumador = sumador + x
    return sumador
y = suma_total([6,3, -2])
print(y)


# 4 Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
# Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

def promedio(promediar):
    sumador = 0
    for x in promediar:
        sumador = sumador + x
    return sumador/len(promediar)
u = promedio([1,2,3,4])
print(u)


# 5 Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
# Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
# Ejemplo: longitud ([]) debería devolver 0

def longitud(medir):
    return len(medir)
s = longitud([])
print(s)

def longitud(medir):
    contador = 0
    for x in medir:
        contador = contador + 1
    return contador
s = longitud([37,2,1, -9])
print(s)


# 6 Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
# Ejemplo: mínimo ([]) debería devolver False

def f_minimo(buscar):
    if len(buscar) == 0:
        return False
    else:
        min = buscar[0]
        for x in range(0,len(buscar)):
            if min > buscar[x]:
                min = buscar[x]
        return min
c = f_minimo([])
print (c)


# 7 Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
# Ejemplo: máximo ([]) debería devolver False

def maximo(buscar):
    if len(buscar) == 0:
        return False
    else:
        max = buscar[0]
        for x in range(0,len(buscar)):
            if max < buscar[x]:
                max = buscar[x]
        return max
u = maximo([37,2,1, -9])
print(u)


# 8 Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
# Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'totalTotal': 31, 'promedio': 7.75, 'mínimo': -9, 'máximo': 37, 'longitud': 4}

def analysis(calc):
    maximo = calc[0]
    minimo = calc[0]
    suma_total = 0
    for i in range(0, len(calc)):
        suma_total = suma_total + calc[i]
        if maximo < calc[i]:
            maximo = calc[i]
        if minimo > calc[i]:
            minimo = calc[i]
    dictionary = {"suma_total": suma_total, "promedio":suma_total/len(calc), "minimo": minimo,"maximo": maximo, "longitud": len(calc)}
    return dictionary

l = analysis([37,2,1, -9])
print(l)


# 9 Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]

def reverlist(list):
    list.reverse()
    return list
a = reverlist([37,2,1, -9])

print(a)