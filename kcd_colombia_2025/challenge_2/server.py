import http.server
import socketserver
import time

PORT = 80
Handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
except:
    print("Error: Unable to start the service")
    while True:
        time.sleep(10)
