# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26

Name: Don Kuruppu
ID  : #1001 101 220
"""

import sys
import http.client
import time

# -------------------------------------------------------------
# This class implements requirements in the project description
# -------------------------------------------------------------
class ProjectRequirements():
    SERVER = "127.0.0.1"                # Talk to local server by default
    PORT = 8080                         # Use 8080 by default
    FILE = "test.htm"                   # Receive this by default

    # This function checks to see if the user provided the script with args
    def initiation(self):
        
        # Check for how many args user has provided, and check for their validity
        if len(sys.argv) >= 4:
            self.check_server_name(sys.argv[1])
            self.check_port_number(sys.argv[2])
            self.check_file(sys.argv[3])
        elif len(sys.argv) == 3:
            self.check_server_name(sys.argv[1])
            self.check_port_number(sys.argv[2])
            print("User hasn't provided a filename. Default filename is used.\n")
        elif len(sys.argv) == 2:
            self.check_server_name(sys.argv[1])
            print("User hasn't provided a port number. 8080 is used.\n")
            print("User hasn't provided a filename. Default filename is used.\n")
        else:
            print("User hasn't provided any arguments. Default values are used.\n")
    
    # Checks if the user has not given localhost or 127.0.0.1
    def check_server_name(self, name):
        if name == 'localhost' or name == '127.0.0.1':
            self.SERVER = name
        else:
            print("Server name provided is not localhost or 127.0.0.1. Using local server by default.\n")
   
    # Checks to see if user has given a valid port number
    def check_port_number(self, port):
        
        # Try to convert given value for port number to an integer
        try:
            self.PORT = int(sys.argv[2])
        except:
            print("Given port number not acceptable. Using port 8080\n")
            
    # Assigns the path given by the user
    def check_file(self, file):
        self.FILE = file
        

# -----------------------------------------------------------------------
# Creates an http client that listens to given port number on localserver
# -----------------------------------------------------------------------
class HttpClient():    
    
    # Following method instantiates the class
    def __init__(self, server_name, port_number, file_name):
        self.server = server_name
        self.port = port_number
        self.file = file_name
    
    # Following method creates the http request, sends it, and displays 
    # the received file content along with some connection parameters
    def make_request(self):
        connection = http.client.HTTPConnection(self.server + ':' + str(self.port))
        
        try:
            # To calculate RTT get time stap before requesting
            time_req = time.time()
            connection.request("GET", '/' + self.file)
            time_recv = time.time()
        except ConnectionRefusedError:
            print("Connection refused by the server.\n\n")
            return
        
        # Get socket details before getting response as 
        peerName = connection.sock.getpeername()
        socketFamily = connection.sock.family
        socketType  = connection.sock.type
        socketProtocol = connection.sock.proto
        
        try:
            response = connection.getresponse()
        except:
            print("Remote end closed without response.\n\n")
            return
        
        print("\n------------------ Received ---------------------\n")
        
        # Display server header details
        print(response.headers)
        
        # Display http version 
        if response.version == 10:
            print('HTTP/1.0 ')
        elif response.version == 11:
            print('HTTP/1.1 ')
        
        # Display http status code
        if response.code == 200:
            print('200 OK\n\n')
        elif response.code == 404:
            print('404 NOT FOUND\n\n')
            
        # Display received file content
        print(response.read().decode('utf-8') + '\n')
            
        # Display server parameters
        print("RTT: %s\n" % str(time_recv - time_req) +
              "Host Name: %s\n" % connection.host +
              "Server Port Number: %s\n" % connection.port +
              "Peer Name: " + str(peerName) + '\n' +
              "Socket Family: " + str(socketFamily) + '\n' +
              "Socket Type: " + str(socketType) + '\n' +
              "Socket Protocol: " + str(socketProtocol) + '\n\n'
              )
        
        print("-------------------- Done -----------------------\n")
        
        
        connection.close()
     
             
if __name__ == '__main__':
    project = ProjectRequirements()
    project.initiation()
    
    client = HttpClient(project.SERVER, project.PORT, project.FILE)
    client.make_request()


