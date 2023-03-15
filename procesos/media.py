nota1 = input("nota 1: ")
nota2 = input("nota 2: ")
print (type(nota1))
nota1 = int (nota1)
nota2 = int (nota2)
print (type(nota1))
media = ((nota1 + nota2 )/2)
print (type(media))
print ("la nota media es:",media)
if media > 5:
    print ("aprobado")
else:
    print ("suspenso")