import socket
import threading

def start_server():
    host = '127.0.0.1'
    port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)  # Ожидаем только одно соединение

    print(f"[*] Listening on {host}:{port}")

    client_socket, addr = server.accept()
    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

    handle_connection(client_socket)

def start_client():
    host = input("Enter server IP: ")
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print(f"[*] Connected to {host}:{port}")

    handle_connection(client)

def handle_connection(socket):
    while True:
        message = input("Enter message (or 'exit' to quit): ")

        if message.lower() == 'exit':
            break

        socket.send(message.encode('utf-8'))

        data = socket.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")

    socket.close()

def main():
    role = input("Choose role (server/client): ")

    if role.lower() == 'server':
        start_server()
    elif role.lower() == 'client':
        start_client()
    else:
        print("Invalid role. Choose either 'server' or 'client'.")

if __name__ == "__main__":
    main()