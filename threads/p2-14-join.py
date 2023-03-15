import threading
import logging

logging.basicConfig(level=logging.DEBUG,format='[%(threadName)-10s]: %(message)s]')

def imprime_x (x,n):
    logging.debug ("INICIO")
    for i in range(n):
        logging.debug(x)
    logging.debug("FIN")

t1 = threading.Thread(target=imprime_x, args=("norte",5))
t2 = threading.Thread(target=imprime_x, args=("sur",10))

t1.start()
t2.start()

#esperar a que el hilo t1 haya finalizado
t1.join()
#esperar a que el hilo t2 haya finalizado
t2.join()

logging.debug("Fin de mi programa!!!")