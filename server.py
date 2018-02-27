# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 

Name: Don Kuruppu
ID  : #1001 101 220 
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading
import sys
from urllib.parse import urlparse
import glob
import os

# -------------------------------------------------------------
# This class implements requirements in the project description
# -------------------------------------------------------------
class ProjectRequirements():
    HOST = "127.0.0.1"                  # Listening to local server
    PORT = 8080                         # Listening to 8080 by default
    
    PATH_INDEX = 2                      # Url parsing will return a list whose #2 is the path
    DEFAULT_FILE = "./test.htm"         # Name of the file sent in the default case
    ERROR_FILE = "./error.htm"          # Name of the file sent with a 404 response
    
    # This function checks to see if the user provided the script with a port number
    def initiation(self):
        # Checking if user has provided the script with a desired port number
        if len(sys.argv) > 1:
            # Try to convert given value for port number to an integer
            try:
                self.PORT = int(sys.argv[1])
            except:
                print("Given port number not acceptable. Using port 8080\n")
        else:
            print("Port number not provided by user. Using 8080 for port.\n")

# This functions checks to see if the path to the file provided by a client exists
def file_exists(filename):
    # If the filename is '/'
    if filename == '/':
        return ProjectRequirements.DEFAULT_FILE
        # Check if the path is valid
        else:
            paths = glob.glob("." + filename)
            
            # If path has no elements, path name is not valid
            if paths == []:
                return ProjectRequirements.ERROR_FILE
            # Else, check to see if folder or file and then return
            else:
                for name in paths:
                    # Return as soon as a file is found
                    if os.path.isfile(name):
                        return name
    
                # If no such file found return the error file
        return ProjectRequirements.ERROR_FILE

# ---------------------------------------------------
# This class handles incoming get requests by clients
# ---------------------------------------------------
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        filepath = ProjectRequirements.file_exists(urlparse(self.path)[ProjectRequirements.PATH_INDEX])
        
        # File requested doesn't exit
        if filepath == ProjectRequirements.ERROR_FILE:
            self.send_response(404)
            self.end_headers()
            
            # Important to open as 'rb'. Otherwise will have to encode the final result
            with open(filepath, 'rb') as fUploadFile:
                uploadFile = fUploadFile.read()
                uploadFile = uploadFile + ("served by " + threading.currentThread().getName()).encode('utf-8')
                self.wfile.write(uploadFile)
        # File exists
        else:
            self.send_response(200)
            self.end_headers()
            
            # Important to open as 'rb'. Otherwise will have to encode the final result
            with open(filepath, 'rb') as fUploadFile:
                uploadFile = fUploadFile.read()
                uploadFile = uploadFile + ("served by " + threading.currentThread().getName()).encode('utf-8')
                self.wfile.write(uploadFile)

    return

# -------------------------------------------------------
# This class handles threading portion for the httpserver
# -------------------------------------------------------
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


if __name__ == '__main__':
    project = ProjectRequirements()
    project.initiation()
    
    try:
        httpServer = ThreadedHTTPServer((project.HOST, project.PORT), RequestHandler)
        print('Starting server ....\n')
        httpServer.serve_forever()
    # Upon encountering a keyboard interrupt, close the server before existing
    except KeyboardInterrupt:
        httpServer.server_close()
            
    
