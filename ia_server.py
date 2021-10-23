#IMPORTAR LAS LIBRERIAS 
from urllib import parse
from http.server import BaseHTTPRequestHandler, HTTPServer

#Codigo de entrenamiento de IA

#servidor en Python
class servidorBasico(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Peticion recibida por GET")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Hola Mundo desde Python, GRUPO 8".encode())

    def do_POST(self):
        print("Peticion recibida por POST")
        #obtenemos los datos enviados por AJAX => Asincrono JavaScript y XML
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        data = data.decode('utf-8')
        print(data)

print("Iniciando el servidor de Python")
servidor = HTTPServer(("localhost", 3008), servidorBasico)
servidor.serve_forever()