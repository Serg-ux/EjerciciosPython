import threading

def thread_apellido(name):
    print (name + " Rodriguez")

nombres = ["Julio", "Javier", "Eladio", "Jose", "Guillen"]
hilos = list()
for n in nombres:
    t = threading.Thread (target=thread_apellido, args=(n,))
    hilos.append(t)
    t.start()
