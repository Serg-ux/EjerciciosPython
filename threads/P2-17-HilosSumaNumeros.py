""" Programa que ejecute 10 hilos, cada uno de los cuales sumará 100 números aleatorios entre el 1 y el 1000. 
Mostrar el resultado de cada hilo. 
Gana el hilo que consiga el número más alto. (TODAVÍA NO RESUELTO AQUI)
 """
from threading import Thread
import random

def suma100aleatorios():
    suma = 0
    for _ in range (100):
        suma += random.randint(1,1000)
    print (suma)

lista_hilos = []
for _ in range (10):
    lista_hilos.append(Thread(target=suma100aleatorios))
    lista_hilos[-1].start()

for t in lista_hilos:
    t.join()

#print (g)