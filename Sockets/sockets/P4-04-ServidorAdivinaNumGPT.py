import random
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 2000)
print(f"starting up on {server_address}")
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()

    try:
        print(f"connection from {client_address}")
        # Generate a random number
        number = random.randint(1, 100)

        # Receive the client's guess
        data = connection.recv(16)
        guess = int(data.decode())

        # Send feedback to the client
        if guess == number:
            connection.sendall(b"Correct!")
        elif guess < number:
            connection.sendall(b"Too low.")
        else:
            connection.sendall(b"Too high.")

    finally:
        # Clean up the connection
        connection.close()