""" Programa que ejecute 10 hilos, cada uno de los cuales sumará 100 números aleatorios entre el 1 y el 1000. 
Mostrar el resultado de cada hilo. 
Gana el hilo que consiga el número más alto.
 """

import threading 
import random

def suma100aleatorios():
    global mayor_suma, mejor_hilo
    suma = 0
    for _ in range (100):
        suma += random.randint(1,1000)
    print (suma)
    with candado:
        if (suma >mayor_suma):
            mayor_suma = suma
            mejor_hilo = threading.current_thread().name

mayor_suma = 0
mejor_hilo = ""
lista_hilos = []
candado = threading.Lock()
for _ in range (10):
    lista_hilos.append(threading.Thread(target=suma100aleatorios))
    lista_hilos[-1].start()

for t in lista_hilos:
    t.join()

print (mejor_hilo)