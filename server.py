from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import mysql.connector
import json
import math
from PIL import Image
import numpy as np
# Crear una ai que reconozca el rostro
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2
from keras.models import load_model

class analizar_rostro():
    def __init__(self):
        self.model = load_model('model.hdf5')

    def cargar_imagen(self, ruta):
        imagen = cv2.imread(ruta)
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        return imagen

    def dibujar_rostro(self, imagen, title=''):
        fig = plt.figure(figsize=(8, 8))
        ax1 = fig.add_subplot(111)
        ax1.set_yticklabels([])
        ax1.set_xticklabels([])
        
        ax1.set_title(title)
        ax1.imshow(imagen)
        plt.show()

    def dame_rostro(self, imagen):
        copia_imagen = np.copy(imagen)
        
        gray = cv2.cvtColor(copia_imagen, cv2.COLOR_BGR2GRAY)

        clasificador = cv2.CascadeClassifier('detectors/haarcascade_frontalface_default.xml')

        cara = clasificador.detectMultiScale(gray, 1.2, 4)

        return cara

    def dibujar_rectangulo(self, imagen, cara=None, plot=True):
        if cara is None:
            cara = self.dame_rostro(imagen)
        
        imagen_con_rectangulo = np.copy(imagen)

        for (x, y, w, h) in cara:
            cv2.rectangle(imagen_con_rectangulo, (x, y), (x + w, y + h), (255, 0, 0), 3)

        if plot is True:
            self.dibujar_rostro(imagen_con_rectangulo)
        else:
            return imagen_con_rectangulo

    def pintar_puntos(self, imagen, informacion_imagen):
        fig = plt.figure(figsize=(8, 8))
        ax1 = fig.add_subplot(111)

        for (cara, puntos) in informacion_imagen:
            for (x, y) in puntos: ax1.scatter(x, y, s=10, c='c', marker='o')

        ax1.set_yticklabels([])
        ax1.set_xticklabels([])
        ax1.imshow(imagen)

    def analizar(self, img):
        img = cv2.resize(img, (64, 64))
        img = np.reshape(img, (1, 64, 64, 3))
        img = img / 255.0
        pred = self.model.predict(img)
        return pred

detectar_rostro = analizar_rostro()
imagen = detectar_rostro.cargar_imagen('icon/breaking_bad.jpg')
cara = detectar_rostro.dame_rostro(imagen)
print("Caras detectadas {}".format(len(cara)))
imagen_con_rectangulo = detectar_rostro.dibujar_rectangulo(imagen, cara)

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
        id = 0
        if datos['accion'] == 'nuevo':
            sql = 'INSERT INTO pacientes (idPaciente, DUI, NIT, Nombre, Sexo, Telefono, Correo, Direccion, FechaNacimiento, Foto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            id = self.auto_increment('pacientes')
            valores = (id, datos['dui'], datos['nit'], datos['nombre'], datos['sexo'], datos['telefono'], datos['correo'], datos['direccion'], datos['fechaNacimiento'], 'icon/pacientes/perfil'+str(id)+'.jpg')
            resultado = self.ejecutar_sql(sql, valores)
            if resultado == True:
                mensaje = 'Paciente registrado exitosamente'
            else:
                mensaje = 'Error al registrar paciente'
        elif datos['accion'] == 'editar':
            sql = 'UPDATE pacientes SET DUI = %s, NIT = %s, Nombre = %s, Sexo = %s, Telefono = %s, Correo = %s, Direccion = %s, FechaNacimiento = %s WHERE idPaciente = %s'
            valores = (datos['dui'], datos['nit'], datos['nombre'], datos['sexo'], datos['telefono'], datos['correo'], datos['direccion'], datos['fechaNacimiento'], datos['id'])
            resultado = self.ejecutar_sql(sql, valores)
            if resultado == True:
                mensaje = 'Paciente editado exitosamente'
            else:
                mensaje = 'Error al editar paciente'

        datos = {'respuesta': resultado, 'mensaje': mensaje, 'id': id}
        return datos

    def permitir_entrada(self, usuario):
        # Se llamara a la ai para detectar el rostro
        # Si el rostro es reconocido, se permitira el acceso
        # Si no, se denegara el acceso
        return True

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

        elif self.path == '/admintir':
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            data = data.decode('utf-8')
            data = json.loads(data)
            resultado = crud.permitir_entrada(data)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resultado=resultado)).encode('utf-8'))

print('Servidor iniciado en el puerto 3008')
servidor = HTTPServer(('localhost', 3008), servidorBasico)
servidor.serve_forever()