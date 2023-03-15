from threading import *
import time

#los hilos por defecto estan con daemon=false

def hilo():				
  for i in range(10):
    print('Hilo no Daemon (Foregoround)')
    time.sleep(1)

t = Thread(target=hilo)
t.start()	

time.sleep(5)				
print('Hilo principal')