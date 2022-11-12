import threading
#def es para definir funciones
def actividad():
    print("escribo desde un hilo")
    return
print ("inicio")
hilos=list()
for i in range(50):
    t=threading.Thread(target=actividad)
    hilos.append(t)
    t.start()
print("escribo desde el principal")