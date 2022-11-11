
"""
Created on Thu Sep 15 10:44:53 2022

@author: bhaveshjain
"""

import socket

import encryption
import os
import utilities

import base64
host= '10.0.0.1'
port=8751

def server(client_socket, address):
    try:
        #receiving key and request from the client
        key=int(utilities.recv_msg(client_socket))
        print("Encrytion key: ", key)
        request=utilities.recv_msg(client_socket)
        

        
        response='default'
        #decrypting the request on the basis of the key
        if(key==1):
            request=encryption.decode1(request)
        elif(key==2):
            request=encryption.transpose(request)
        elif(key==0):
            pass
        else:
            print("Key is invalid")
        
        print("Hi, I am server, client requested for: ", request)
        
        l=request.split()
        
        
        if request=="cwd":
            response = utilities.curr_dir()
       
        
        
                
        elif l[0]=="upd":
            file=l[1]
            with open(file, 'wb') as f:
                i=0
                while(True):
                    #recieving the data in base64 encoding
                    data = client_socket.recv(1368)
                    i+=len(data)
                    print("Recieved: ", len(data), "   Total Recieved: ", i)
                    data=data.decode("ascii")
                    #decrypting the data on the basis of the key
                    if key==1:
                        data=encryption.decode1(data)
                    if key==2:
                        data=encryption.transpose(data)
                    if key==0:
                        pass
                    c= data.encode("ascii")
                    
                    if not data:
                        print("Download Complete")
                        f.close()
                        break
                    #writing the data in the file
                    f.write((base64.b64decode((c))))
                f.close()        
        
        
        elif l[0]=="dwd":
            file=l[1]
            
            with open(file, 'rb') as f:
                i=0
                while(True):
                    #reading the data from file and encoding it in base64 format.
                    data = base64.b64encode(f.read(1024))
                    c = data.decode("ascii")
                    # Encrytping the data on the basis of the key
                    if key==1:
                        c=encryption.encode1(c)
                    if key==2:
                        c=encryption.transpose(c)
                    if key==0:
                        pass
                    data = c.encode("ascii")
                    i+=len(data)
                    #sending the data
                    print("Sending: ", len(data), "   Total Sent:", i  )
                    if not data:
                        break
                    client_socket.sendall(data)

            f.close()
        #for ls command and cd command
        elif request=="ls":
            path=utilities.curr_dir()
            response=str(utilities.ls(path))
         
        elif l[0]=="cd":
            path=l[1]
            if (path in os.listdir()) or path=="..":
                response=utilities.change_dir(path)
            else:
                response="Directory does not exist"

        #if the request are not upd/dwd(in which the response has already been sent) sending the response to the client
        #the response is encrypted using the key
        if(l[0]!="upd" and l[0]!="dwd"):
            print("sending response")
            if key==0:
                utilities.send_msg(client_socket, response)
            elif key==1:
                utilities.send_msg(client_socket, encryption.encode1(response))
            elif key==2:
                utilities.send_msg(client_socket, encryption.transpose(response))
        
        
        print("Connection Terminated!")
        client_socket.close()
        

    except:
        print("Error!")
        client_socket.close()

        




#creating the socket
server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(5)

print('Listening on: ', (host, port))

while True:
    (client_socket, address) = server_socket.accept()
    print("Connected to: ",address)
    server(client_socket, address)
