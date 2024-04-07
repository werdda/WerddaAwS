from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class RequestResponser(BaseHTTPRequestHandler):
    
    def do_GET(self):
       if self.path == '/':
           self.send_response(200)
           self.send_header('Content-type', 'text/plain')
           self.end_headers()
           message = "Hello World"
           self.wfile.write(message.encode('utf-8'))
       elif self.path == '/endpoint1':
           self.send_response(200)
           self.send_header('Content-type', 'text/plain')
           self.end_headers()
           message = "Response from endpoint 1"
           self.wfile.write(message.encode('utf-8'))

       else:
           self.send_response(200)
           self.send_header('Content-type', 'text/plain')
           self.end_headers()
           message = "404 not found" 
           self.wfile.write(message.encode('utf-8'))  
        
        
        
def run(serverClass = HTTPServer, serverResponse = RequestResponser, port = 5000):
    server_address = ('', port)
    httpd = serverClass(server_address, serverResponse)
    print(f'Starting Sever on Port {port}...')
    httpd.serve_forever()
    
    
if __name__ == '__main__':
    run()