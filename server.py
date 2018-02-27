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
