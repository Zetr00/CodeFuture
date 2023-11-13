import socket
import pickle
from myClass import MyClass

host = '127.0.0.1'
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
print(f"[*] Listening on {host}:{port}")

while True:
    client, addr = server.accept()
    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

    data = client.recv(1024)
    if not data:
        break

    received_object = pickle.loads(data)

    print("Received object:")
    print(received_object.get_info())

    received_object.increment_age()

    print("Updated object:")
    print(received_object.get_info())

    client.close()