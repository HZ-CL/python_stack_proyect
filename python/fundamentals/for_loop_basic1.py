# 1 Básico : imprime todos los enteros del 0 al 150.

for x in range(0, 150,1):
    print(x)


# 2 Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000

for x in range(5,1000):
    if x % 5 == 0:
        print(x)


# 3 Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5,
# imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".

for x in range(1,100):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else :
        print(x)


# 4 ¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.


suma = 0;
for x in range(0, 500000):
    if x % 2 !=0:
        suma = suma + x;
print(suma)


# 5 Cuenta regresiva por cuatro : imprime números positivos a partir de 2018,
#  cuenta atrás por cuatro.

for x in range(2018, 0,-4):
    print(x)


# 6 Contador flexible : establece tres variables: lowNum, highNum, mult.
# Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult.
# Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)

lowNum = 2;
highNum = 9;
mult = 3;

for x in range(lowNum, highNum+1):
    if x % mult ==0:
        print(x)




