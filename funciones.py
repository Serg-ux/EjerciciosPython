def suma2(a, b):
    return a+b
x = suma2(5, 3) 
print (x)


def suma2(a, b=5):
    return a+b
x = suma2(5, 3) 
y = suma2(2)
print (x)
print (y)

def cuentMult3(n):
    x=range(0,n+1)
for b in x:
    if n%3==0:
        print(b)

cuentMult3(5)