#!/Users/mieter/miniconda3/bin/python

import http.server
import socketserver

## A simple script to use the python CGI server.
## Using CGIHTTPRequestHandler in place of SimpleHTTPRequestHandler
## allows python scripts to be called as an action (POST)

#define the handler to be the CGI server
handler = http.server.CGIHTTPRequestHandler

#point the handler to a directory with scripts
handler.cgi_directories = ["/python-scripts"]

# define the server usinh the handler
PORT = 8000
httpd = socketserver.TCPServer(("localhost",PORT), handler)

## Set variables which the CGIHTTPRequestHandler expects
httpd.server_name = "myServer"
httpd.server_port = PORT

#run the server. To kill it, issue Ctrl + C
httpd.serve_forever()
