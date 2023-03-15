from threading import Thread
import time

def suma_uno():
    global g
    a = g
    time.sleep(0.0001)
    g = a + 1

def suma_tres():
    global g
    a = g
    time.sleep(0.0001)
    g = a + 3

g = 0
lista_hilos = []
for func in [suma_uno,suma_tres]:
    lista_hilos.append(Thread(target=func))
    lista_hilos[-1].start()

for t in lista_hilos:
    t.join()

print (g)