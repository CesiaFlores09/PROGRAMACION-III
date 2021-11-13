from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import mysql.connector
import json

class crud:
    def __init__(self):
        self.conexion = mysql.connector.connect(user='root', password='',
                                           host='localhost', database='db_login')
        if self.conexion.is_connected():
            print('Conectado exitosamente a la base de datos')
        else:
            print('Error al conectar a la base de datos')

    


class servidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
            return SimpleHTTPRequestHandler.do_GET(self)


    def do_POST(self):
        if self.path == '/insertar':
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            data = data.decode('utf-8')
            data = json.loads(data)
            self.send_response(200)
            self.end_headers()
           

print('Servidor iniciado en el puerto 3008')
servidor = HTTPServer(('localhost', 3008), servidorBasico)
servidor.serve_forever()