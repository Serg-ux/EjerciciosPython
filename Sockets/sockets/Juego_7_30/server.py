import random
import socket
import threading

valores_cartas = {
    "As": 1, "Dos": 2, "Tres": 3, "Cuatro": 4,
    "Cinco": 5, "Seis": 6, "Siete": 7, "Sota": 0.5,
    "Caballo": 0.5, "Rey": 0.5
}

#coge los una carta al azar de la lista y coge su valor y su nombre
def obtener_carta():
    carta = random.choice(list(valores_cartas.keys()))
    valor = valores_cartas[carta]
    return carta, valor

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 5000))
servidor.listen()
print("Servidor escuchando en localhost:5000")

while True:
    cliente, direccion = servidor.accept()
    print(f"Conexión establecida desde {direccion}")
    carta, valor = obtener_carta()
    cliente.send(f"{carta},{valor}".encode())
    cliente.close()
