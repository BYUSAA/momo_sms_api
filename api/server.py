from http.server import HTTPServer
from api.routes import RequestHandler

def run_server():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("✅ Server running at http://localhost:8000")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
