from http.server import SimpleHTTPRequestHandler, HTTPServer

class SimpleServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Hello, Docker!</h1></body></html>")

if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleServer)
    print("Server running on port 8000...")
    httpd.serve_forever()