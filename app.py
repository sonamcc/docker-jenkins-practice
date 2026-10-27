
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

message = os.getenv("MESSAGE", "Hello from my Docker image!")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

server = HTTPServer(("0.0.0.0", 8000), Handler)
print("Application is running on port 8000")
server.serve_forever()
