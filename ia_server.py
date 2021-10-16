
from urllib import parse
from http.server import BaseHTTPRequestHandler, HTTPServer

#Codigo de entrenamiento IA

#Servidor en python
class servidorBasico(BaseHTTPRequestHandler):
    def do_GET(self):
        print("PETICION RECIBIDA POR POST")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("Hola Mundo desde Python".encode()))

    def do_POST(self):
        print("Peticion recibida por GET")
        #obtenemos los datos enviados por AJAX
        content_length = int(self.headers['Content-Length'])
        data=self.rfile.read(content_length)
        data=data.decode('utf-8')
        print(data)

        
print("Iniciando el servidor de Python")
servidor = HTTPServer(("localhost", 8000), servidorBasico)
servidor.serve_forever()
