from statistics import median


print("Introduzca dos numeros para sacar su media")
num1=float(input())
num2=float(input())
suma=num1+num2
media=suma/2
print(media)
if media<5:
    print("estás suspenso")
else:
    print("estás aprobado")
