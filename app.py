from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/error":
            print("ERROR: simulated failure", flush=True)
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Internal Server Error")
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello from Python in Docker Compose!")

if __name__ == "__main__":
    print("Server running on port 5000", flush=True)
    server = HTTPServer(("0.0.0.0", 5000), MyHandler)
    server.serve_forever()
