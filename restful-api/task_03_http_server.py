#!/usr/bin/python3

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Handle the /data endpoint
        if self.path == '/data':
            # JSON response
            response_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)  # OK
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode())

        # Handle the /status endpoint
        elif self.path == '/status':
            # Text response for status
            self.send_response(200)  # OK
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        # Handle the /info endpoint
        elif self.path == '/info':
            # JSON response for version and description
            response_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)  # OK
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode())

        # Handle undefined endpoints
        else:
            self.send_response(404)  # Not Found
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    # Set up and start the server
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
