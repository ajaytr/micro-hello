import datetime
import os

from http.server import BaseHTTPRequestHandler
from socketserver import UnixStreamServer  # Use UnixStreamServer for UNIX sockets

# HTTPRequestHandler class
class BasicUDSServerRequestHandler(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "Python says: Hello World!\n"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return


if __name__ == "__main__":
    now = datetime.datetime.now()
    server_address = '/tmp/py-hello.sock'

    # First remove the socket file if it already exists
    try:
        os.unlink(server_address)
    except OSError:
        if os.path.exists(server_address):
            raise

    print("Starting server at time: " + str(now) + ", at address: " + server_address + "\n")

    # Server settings
    httpd = UnixStreamServer(server_address, BasicUDSServerRequestHandler)
    httpd.serve_forever()
