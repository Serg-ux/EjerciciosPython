import logging
import random
import threading
import time

logging.basicConfig( level=logging.DEBUG,
    format='[%(threadName)-10s]: %(message)s')

def cubrir_carton(num_jug):
    global carton
    for _ in range(NUMEROS_CARTON):
        carton[num_jug].append(random.randint(1,MAX_NUM))

def sacar_bola():
    global bola_actual
    while True:
        if ganador !=-1:
            break
        bola_actual = random.randint(1,MAX_NUM)
        logging.debug (f"bolita {bola_actual}")
        time.sleep(1)

def tachar_carton(num_jug):
    global carton
    bola_comparar = -1
    while True:
        if bola_actual !=bola_comparar:
            bola_comparar= bola_actual
            for b in carton[num_jug]:
                #logging.debug(f"carton {b}")
                #logging.debug(f"comparar con {bola_actual}")
                if (b==bola_actual):
                    #logging.debug ("tachado")
                    carton[num_jug].remove(b)
                    logging.debug(carton)
                    break

def comprobar_carton(num_jug):
    global ganador
    while True:
        if len (carton[num_jug]) == 0: #si la lista está vacía
            ganador=num_jug
            break

def arbitro():
    while True:
        if ganador !=-1:
            print (f"El ganador es: {ganador+1}")
            print (carton)
            break
   


JUGADORES=5
MAX_NUM = 20
NUMEROS_CARTON=4
bola_actual=0
ganador = -1
hilos = list()
hilostc = list()
carton=[]

for i in range(JUGADORES):
    carton.append([])
    t = threading.Thread(target=cubrir_carton, args=(i,))
    hilos.append(t)
    t.start()


logging.debug(carton)

for t in hilos:
    t.join()
hilos.clear()

sb = threading.Thread(target=sacar_bola)
sb.start()

for i in range(JUGADORES):    
    t = threading.Thread(target=tachar_carton, args=[i]) 
    hilos.append(t)
    t.start()

for i in range(JUGADORES):    
    t = threading.Thread(target=comprobar_carton, args=[i]) 
    hilos.append(t)
    t.start()

juez = threading.Thread(target=arbitro)
juez.start()
