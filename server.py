from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import mysql.connector
import json

class crud:
    def __init__(self):
        self.conexion = mysql.connector.connect(user='root', password='',
                                           host='localhost', database='db_cliente')
        if self.conexion.is_connected():
            print('Conectado exitosamente a la base de datos')
        else:
            print('Error al conectar a la base de datos')

    def insertar(self, codigo, nombre, telefono, direccion, email, sexo, fecha):
        try:
            cursor = self.conexion.cursor()
            sql = "INSERT INTO Cliente (codigo, nombre, telefono, direccion, email, sexo, fecha) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (codigo, nombre, telefono, direccion, email, sexo, fecha)
            cursor.execute(sql, val)
            self.conexion.commit()
            return 'Registro insertado correctamente'
        except Exception as e:
            return str(e)

crud = crud()
class servidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
            return SimpleHTTPRequestHandler.do_GET(self)

    def do_Post(self):
        if self.path == '/insertar':
            content_lenght = int(self.headers['Content-Length'])
            data = self.rfile.read(content_lenght)
            data = data.decode('utf-8')
            data = parse.unquote(data)
            data = json.loads(data)
            resp = crud.insertar(data['codigo'], data['nombre'], data['telefono'], data['direccion'], data['email'], data['sexo'], data['fecha'])
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))


print('Servidor iniciado en el puerto 3008')
servidor = HTTPServer(('localhost', 3008), servidorBasico)
servidor.serve_forever()