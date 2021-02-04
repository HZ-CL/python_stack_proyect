class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        #print("sumas",num,nums)
        addtupla=0
        for i in nums:
            addtupla += i
        self.result += num+addtupla
        return self
    def subtract(self, num, *nums):
        #print("restas", num, nums)
        subtupla = 0
        for i in nums:
            subtupla -=i
        self.result -= num-subtupla
        return self

# crear una instruccion:
md = MathDojo()
# para probar:
x = md.add(2).result
y=md.add(2,5,11).result
z=md.subtract(33,2).result

print("print de x =", x)# output 2
print("print de y =", y)# output 20
print("print de z =", z)# output -15

w=md.add(5).add(3,4,7,1).subtract(12).result
print("Print w =", w)#output -7
