from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import mysql.connector
import json

class crud:
    def __init__(self):
         self.conexion= mysql.connector.connect(user='root', password='',
                                        host='localhost', database='db_academica')
         if self.conexion.is_connected():
             print("Conectado existosamente")

    
class servidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/':
            self.path = '/index1.html'
            return  SimpleHTTPRequestHandler.do_GET(self)
    
    def do_POST(self):
        if self.path =='/insertar':
            content_length = int(self.headers['Content-Length'])
            data= self.rfile.read(content_length)
            data=data.decode('utf-8')
            data=parse.unquote(data)
            data=json.loads(data)
          
           
   
print('Servidor iniciado en el puerto 3000')
servidor= HTTPServer(('localhost',3000),servidorBasico)
servidor.serve_forever()
        