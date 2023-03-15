import threading
import time


def tarea():
  #hace que tarde un segundo en iniciarse el thread
  time.sleep(1)
  return

for _ in range(10):
  threading.Thread(target=tarea).start()

print ("Hilos activos: ",threading.active_count())
for thread in threading.enumerate():
    print(thread.name)