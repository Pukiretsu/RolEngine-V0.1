import socket
import pickle
'''
Description
-------------
Module for server client implementation.
'''
HEADERSIZE = 10

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((socket.gethostname(),1235)) #Here we set the ip and the port

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = c.recv(19) # Message buffering
        
        if new_msg:
            print(f"New msg lenght {msg[:HEADERSIZE]}") # Log line
            msg_len = int(msg[:HEADERSIZE]) 
            
            new_msg = False
        
        full_msg += msg # Builing msg
        
        if len(full_msg) - HEADERSIZE == msg_len:
            
            print("Full msg recvd") # Debuggin line
            
            print(full_msg[HEADERSIZE:]) #Message print
            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)
            
            new_msg = True
            full_msg = b''
    
    print(full_msg)