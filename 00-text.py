from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 클라이언트의 IP 주소를 가져옵니다.
        visitor_ip = self.client_address[0]
        message = f"Your IP address is {visitor_ip}"

        # 응답을 작성하고 반환합니다.
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
