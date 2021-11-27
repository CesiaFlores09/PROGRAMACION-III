from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import mysql.connector
import json
import numpy as np
from PIL import Image

class crud:
    def __init__(self):
        self.conexion = mysql.connector.connect(user='root', password='flores',
                                           host='localhost', database='clinica')
        if self.conexion.is_connected():
            print('Conectado exitosamente a la base de datos')
        else:
            print('Error al conectar a la base de datos')
    def auto_increment(self, tabla):
        try:
            if tabla == 'pacientes':
                sql = 'SELECT MAX(idPaciente) AS id FROM pacientes'
            elif tabla == 'personal':
                sql = 'SELECT MAX(idPersonal) AS id FROM personal'
            valores = ()
            resultado = self.ejercer_consulta(sql, valores)
            if resultado[0]['id'] is None:
                return 0
            else:
                return resultado[0]['id']+1
        except Exception as e:
            print(e)
            return False

    def ejecutar_sql(self, sql, valores):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql, valores)
            self.conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    def ejercer_consulta(self, sql, valores):
        try:
            cursor = self.conexion.cursor(dictionary=True)
            cursor.execute(sql, valores)
            resultado = cursor.fetchall()
            return resultado
        except Exception as e:
            print(e)
            return False

    def administrar_paciente(self, datos):
        if datos['accion'] == 'nuevo':
            sql = 'INSERT INTO pacientes (idPaciente, DUI, NIT, Nombre, Sexo, Telefono, Correo, Direccion, FechaNacimiento, Foto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            id = self.auto_increment('pacientes')
            valores = (id, datos['dui'], datos['nit'], datos['nombre'], datos['sexo'], datos['telefono'], datos['correo'], datos['direccion'], datos['fechaNacimiento'], 'icon/pacientes/perfil'+str(id)+'.jpg')
            resultado = self.ejecutar_sql(sql, valores)
            if resultado != False:
                mensaje = 'Paciente registrado exitosamente'
            else:
                mensaje = 'Error al registrar paciente'
            datos = {'respuesta': resultado, 'mensaje': mensaje, 'id': id}
            return datos

crud=crud()


class servidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
            return SimpleHTTPRequestHandler.do_GET(self)

        else:
            return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/insertar':
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            data = data.decode('utf-8')
            data = json.loads(data)
            self.send_response(200)
            self.end_headers()
           
        elif self.path == '/registrar_paciente':
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            data = data.decode('utf-8')
            data = json.loads(data)
            resultado = crud.administrar_paciente(data)
            print(resultado)
            if data['accion'] == 'nuevo' and resultado['respuesta'] == True:
                matriz = data['foto']
                matriz = [matriz[i:i+200] for i in range(0, len(matriz), 200)]
                matriz = np.array(matriz)
                id = resultado['id']
                im = Image.fromarray((matriz).astype(np.uint8))
                im.save('icon/pacientes/perfil'+str(id)+'.jpg')
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resultado=resultado)).encode('utf-8'))


           

print('Servidor iniciado en el puerto 3008')
servidor = HTTPServer(('localhost', 3008), servidorBasico)
servidor.serve_forever()