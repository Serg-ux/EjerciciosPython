import socket

HOST = '127.0.0.1' 
#HOST = '10.10.32.50' 
PORT = 2000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST,PORT))
    #acepta solo una conexion entrante
    s.listen(1)
    #while (True):
    conn, addr = s.accept() #función bloqueante bloquea la ejecución del programa hasta que se reciba una conexión.
    print (f"Conexión exitosa con el cliente. IP ({addr[0]}) Puerto ({addr[1]})")
    #conn.close()
except socket.error as exc:
    print ("Excepción de socket: %s" % exc)
finally:
    s.close()