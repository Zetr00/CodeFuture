import socket

messages = ["Hello, Server!", "How are you?", "Goodbye!"]

host = '127.0.0.1'
port = 5555

for message in messages:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send(message.encode('utf-8'))
    client.close()
