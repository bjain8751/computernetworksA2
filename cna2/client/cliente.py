
"""
Created on Thu Sep 15 10:45:22 2022

@author: bhaveshjain
"""

import socket
import sys
import encryption
import os
import utilities
import base64
import time

host= '10.0.0.1'
port=8751

while True:
    try:
        #creating and connecting socket
        client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print("Conected to: ", (host, port))
        

        key = input("Please select encrytion key \n0)PlainText 1)Subsitute 2)Transpose \n")
        utilities.send_msg(client_socket, key) #taking key from the user and sending it to the server
        #key is taken as an integer
        key=int(key)
        
        request=input("Please enter your command(or quit): ")
        
        
        l=request.split()
        #breaking the request for processing multi-word requests
        if request=="Quit":
            print("Exiting...")
            break
        
        
        
        
        elif l[0]== "upd":
            #sending the request and encrypting it with key
            start=time.time()
            if key==1:
                request=encryption.encode1(request)
            if key==2:
                request=encryption.transpose(request)
            if key==0:
                pass
              
            utilities.send_msg(client_socket, request)
            file=l[1]            
            with open(file, 'rb') as f:
                i=0
                while(True):
                    ##reading the data from file and encoding it in base64 format.
                    data = base64.b64encode(f.read(1024))
                    c = data.decode("ascii")
                    #encryptng the data according to the key
                    if key==1:
                        c=encryption.encode1(c)
                    if key==2:

                        c=encryption.transpose(c)

                    if key==0:
                        pass
                    data = c.encode("ascii")
                    i+=len(data)
                    #sending the data to the server
                    print("Sending: ", len(data), "   Total Sent:", i  )
                    if (not data):
                        break

                    client_socket.sendall(data)

            print("Upload Success")
            end=time.time()-start
            print("Time taken: ", end, "s")
            f.close()
                
            
       
        elif l[0]=="dwd":
            #sending the request in enrypted mode
            start=time.time()
            if key==1:
                request=encryption.encode1(request)
            if key==2:
                request=encryption.transpose(request)
            if key==0:
                pass
            
            utilities.send_msg(client_socket, request)         
            
            file=l[1]
                       
            with open(file, 'wb') as f:
                i=0
                while(True):
                    #recieving the data
                    data = client_socket.recv(1368)
                    i+=len(data)
                    print("Recieved: ", len(data), "   Total Recieved: ", i)
                    data=data.decode("ascii")
                    
                    #decrytping the data according to the key
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
                    #writing the data in file
                    f.write((base64.b64decode((c))))
                end=time.time()-start
                print("Time taken: ", end, "s")
                
                f.close()
                


        else:
            #sending request cd, cwd, ls after encrypting them according to the key
            if key==1:
                request=encryption.encode1(request)
            if key==2:
                request=encryption.transpose(request)
            if key==0:
                pass
                
            utilities.send_msg(client_socket, request)
            #recieving the response and decrypting it
            response = utilities.recv_msg(client_socket)
            if key==1:
                response = encryption.decode1(response)
            if key==2:
                response = encryption.transpose(response)

            print("Server Sent: ", response)
        
        client_socket.close()
        print("Connection Terminated\n\n\n")


    except:
        print("Error!")
        print("Connection Terminated")
        client_socket.close()
        break
    
