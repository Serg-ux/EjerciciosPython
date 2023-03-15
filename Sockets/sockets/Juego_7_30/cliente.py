import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 5000))
print("Conectado al servidor en localhost:5000")

cartas_jugador = []

while sum(cartas_jugador) <= 7.5:
    respuesta = cliente.recv(1024).decode()
    carta, valor = respuesta.split(",")
    valor = float(valor)
    cartas_jugador.append(valor)
    print("Tu carta es: " + str(carta))
    print("Tu puntuación actual es: " + str(sum(cartas_jugador)))
    if sum(cartas_jugador) > 7.5:
        print("Has perdido")
        break
    pregunta = input("¿Quieres otra carta? (s/n) ")
    if pregunta.lower() != "s":
        break

if sum(cartas_jugador) <= 7.5:
    print("Has ganado")

cliente.close()
