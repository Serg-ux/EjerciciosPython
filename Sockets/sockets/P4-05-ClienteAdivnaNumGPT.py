import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = ('localhost', 2000)
print(f"connecting to {server_address}")
sock.connect(server_address)

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    sock.sendall(str(guess).encode())
    data = sock.recv(16)
    feedback = data.decode()
    print(feedback)
    if feedback == "Correct!":
        print("Congratulations, you guessed the number!")
        break

sock.close()
