from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import mysql.connector
import json

class crud:
    def __init__(self):
        self.conexion = mysql.connector.connect(user='root', password='',
                                           host='localhost', database='cliente')
        if self.conexion.is_connected():
            print('Conectado exitosamente a la base de datos')
        else:
            print('Error al conectar a la base de datos')

    def consultar(self):
        try:
            cursor = self.conexion.cursor(dictionary=True)
            sql = "SELECT * FROM cliente"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            return resultado
        except Exception as e:
            return str(e)

    def ejecutar_consulta(self, sql, val):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql, val)
            self.conexion.commit()
            return "Registro procesado con exito"
        except Exception as e:
            return str(e)

    def administrar_clientes(self, contenido):
        try:
            if contenido["accion"]=="nuevo":
                sql = "INSERT INTO cliente (codigo, nombre, telefono, direccion, email, sexo, fecha) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                val = (contenido["codigo"], contenido["nombre"], contenido["telefono"], contenido["direccion"], contenido["email"], contenido["sexo"], contenido["fecha"])

            elif contenido["accion"]=="modificar":
                sql = "UPDATE cliente SET codigo=%s, nombre=%s, telefono=%s, direccion=%s, email=%s, sexo=%s, fecha=%s WHERE idcliente=%s"
                val = (contenido["codigo"], contenido["nombre"], contenido["telefono"], contenido["direccion"], contenido["email"], contenido["sexo"], contenido["fecha"], contenido["idcliente"])

            elif contenido["accion"]=="eliminar":
                sql = "DELETE FROM cliente WHERE idcliente=%s"
                val = (contenido["idcliente"],)

            return self.ejecutar_consulta(sql, val)
        except Exception as e:
            return str(e)

crud = crud()
class servidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
            return SimpleHTTPRequestHandler.do_GET(self)

        if self.path == '/consultar':
            resp = crud.consultar()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

    def do_POST(self):
        if self.path == '/insertar':
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            data = data.decode('utf-8')
            data = json.loads(data)
            resp = crud.administrar_clientes(data)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

print('Servidor iniciado en el puerto 3008')
servidor = HTTPServer(('localhost', 3008), servidorBasico)
servidor.serve_forever()