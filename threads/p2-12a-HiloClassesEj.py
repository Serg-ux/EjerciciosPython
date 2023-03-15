 #Crear 10 hilos asociados a una clase que permita tener datos de nombre y edad, dándole valores a los nombres y números aleatorios (10-20 a las edades)
#En el método run mostrar solamente los nombres de las personas mayores de 18 años.
#Ejecutar todos los hilos en paralelo
import threading
import random

class miHilo(threading.Thread):
  def __init__(self, nombre):
    super(miHilo, self).__init__()
    self.edad = 0
    self.nombre = nombre
  def run(self):
    if self.edad >= 18:
      print (f'Permitiod el paso a {self.nombre}, porque tiene {self.edad} años\n',end='')
    

ListaHilos = [] #inicio con la lista vacía
nombres = ["Eladio", "Jose", "Manuel", "Julio","Maria","Susana","Emma","Javier","Marcos","Roberto"]
for i in range(10):
  t = miHilo(nombres[i])
  t.edad = random.randint(10, 20)
  ListaHilos.append(t)
for h in ListaHilos:
  h.start()