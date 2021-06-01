import socket
import pickle

'''
Description
-------------
Module for local server implementation.
'''

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5) #The queue

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} stablished!")

    d = {1:"bruh", 2:"moment"}
    msg = pickle.dumps(d)
    
    msg = bytes(f'{len(msg):<{HEADERSIZE}}',"UTF-8") + msg # Header sender

    clientsocket.send(msg)