# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26

Name: Don Kuruppu
ID  : #1001 101 220
"""

import sys
import http.client


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
        if len(sys.argv) == 4:
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
            print("Server name provided is not localserver or 127.0.0.1. Using local server by default.\n")

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
