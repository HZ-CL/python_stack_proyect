#1
def a():
    return 5
print(a()) # return: 5


#2
def a():
    return 5
print(a()+a()) #return : 10


#3
def a():
    return 5
    return 10
print(a())# return : 5


#4
def a():
    return 5
    print(10)
print(a())# return : 5


#5
def a():
    print(5)# 5
x = a()
print(x)# return : none


#6
def a(b,c):
    print(b+c)# print : 3, 5
print(a(1,2)+a(2,3))# return :


#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))# return : 25


#8
def a():
    b = 100
    print(b) # print : 100
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())# return : 10


#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))# return : 7
print(a(5,3))# return : 14
print(a(2,3) + a(5,3))# return : 21


#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))# return : 8


#11
b = 500
print(b) # print : 500 --->1 imprime 500 (valor de la variable)
def a():
    b = 300
    print(b) # print : 300-->2 no se imprime hasta que sea llamada
print(b) # print : 300-->3 imprime 500 (valor antes de def, porque esta afuera de def)
a()# print : 300 --> imprime 300 llamada a def(valor dentro de def)
print(b) # print : 300-->4 imprime 500 (valor antes de def)



#12
b = 500
print(b) # print : 500
def a():
    b = 300
    print(b)
    return b
print(b)# print : 500
a() # return : 300, 300
print(b)# print : 500


#13
b = 500
print(b)# print : 500
def a():
    b = 300
    print(b)
    return b
print(b)# print : 500
b=a() # return : 300
print(b)# print : 300


#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a() # print : 1, 2 --> print 1, 3, 2 (b() dentro de def a(), llama a def b())


#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()# 1, 3, 5
print(y)# print : 10



