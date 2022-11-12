import threading
#metodo que se va a asociar a un hilo
def Saludo():
    print("hola")

t= threading.Thread(target=Saludo)
t.start()

print("Hola") #impresión en el hilo principal