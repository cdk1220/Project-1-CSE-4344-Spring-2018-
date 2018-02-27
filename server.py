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

class ProjectRequirements():
    HOST = "127.0.0.1"        # Listening to local server
    PORT = 8080               # Listening to 8080 by default

    def initiation(self):
        # Checking if user has provided the script with a desired port number
        if len(sys.argv) > 1:
            # Try to convert given value for port number to an integer
            try:
                PORT = int(sys.argv[1])
            except:
                print("Given port number not acceptable. Using port 8080\n")
        else:
            print("Port number not provided by user. Using 8080 for port.\n")

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(urlparse(self.path))
        self.send_response(200)
        self.end_headers()
        message =  threading.currentThread().getName()
        self.wfile.write(message.encode('utf-8'))
        self.wfile.write('\n'.encode('utf-8'))
        return


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


if __name__ == '__main__':
    project = ProjectRequirements()
    project.initiation()
    
    try:
        httpServer = ThreadedHTTPServer((project.HOST, project.PORT), RequestHandler)
        print('Starting server ....\n')
        httpServer.serve_forever()
    except KeyboardInterrupt:
        httpServer.server_close()
            
    
