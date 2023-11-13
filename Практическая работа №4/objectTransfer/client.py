import socket
import pickle
from myClass import MyClass

my_object = MyClass("John", 25)

host = '127.0.0.1'
port = 5555

serialized_object = pickle.dumps(my_object)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

client.send(serialized_object)

client.close()
