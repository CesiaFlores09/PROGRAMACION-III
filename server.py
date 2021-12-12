from types import CellType
from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import random
import string
import numpy as np

import crudpaciente
import crudproveedor
import crudmedicamentos
import crudturnos
import crudespecialidades
import crudpersonal
import crudrecetas
import crudsintoma
import crudenfermedades
import crudcitas
import crudtipoexamen
import crudtipotratamiento
import crudexamenes
import crudtratamientos
import inteligencia

crudproveedor = crudproveedor.curdproveedor()
crudpaciente = crudpaciente.curdpacientes()
crudmedicamentos = crudmedicamentos.curdmedicamento()
crudturnos = crudturnos.curdturno()
crudespecialidades = crudespecialidades.curdespecialidad()
crudpersonal = crudpersonal.curdpersonal()
crudrecetas = crudrecetas.curdreceta()
crudsintoma = crudsintoma.curdsintoma()
crudenfermedades = crudenfermedades.curdenfermedad()
crudcitas = crudcitas.curdcitas()
crudtipoexamen = crudtipoexamen.curdtipo_examen()
crudtipotratamiento = crudtipotratamiento.curdtipo_tratamiento()
crudexamenes = crudexamenes.curdexamen()
crudtratamientos = crudtratamientos.curdtratamiento()
inteligencia = inteligencia.manejarRostros()

paciente = {'id':None, 'dui': None, 'nombre':None}
personal = {'id':None, 'dui': None, 'nombre':None}
token = '----------'

class crud:
    def permitir_entrada(self, usuario):
        return True

class servidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
        global paciente
        global personal
        global token

        if self.path == '/':
            self.path = '/index.html'
            return SimpleHTTPRequestHandler.do_GET(self)

        elif self.path == '/devindex.html' or self.path == '/devregistro.html':
            token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
            print(token)
            return SimpleHTTPRequestHandler.do_GET(self)

        elif self.path == '/consultar-paciente':
            resp = crudpaciente.consultar_paciente()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

        elif self.path == '/consultar-a-paciente':
            resp = crudpaciente.consultar_a_paciente(paciente['id'])
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

        elif self.path == '/consultar-personal':
            resp = crudpersonal.consultar_personal()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

        elif self.path == '/consultar-proveedor':
            resp = crudproveedor.consultar_proveedor()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

        elif self.path == '/consultar-medicamento':
            resp = crudmedicamentos.consultar_medicamento()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

        elif self.path == '/consultar-turno':
            resp = crudturnos.consultar_turno()
            for hora in resp:
                hora['HoraInicio'] = str(hora['HoraInicio'])
                hora['HoraSalida'] = str(hora['HoraSalida'])
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

        elif self.path == '/consultar-especialidad':
            resp = crudespecialidades.consultar_especialidad()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

        elif self.path == '/consultar-receta':
            resp = crudrecetas.consultar_receta()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

        elif self.path == '/consultar-sintoma':
            resp = crudsintoma.consultar_sintoma()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

        elif self.path == '/consultar-enfermedad':
            resp = crudenfermedades.consultar_enfermedad()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

        elif self.path == '/consultar-cita':
            resp = crudcitas.consultar_citas()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

        elif self.path == '/consultar-tipo-examen':
            resp = crudtipoexamen.consultar_tipo_examen()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

        elif self.path == '/consultar-tipo-tratamiento':
            resp = crudtipotratamiento.consultar_tipo_tratamiento()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

        elif self.path == '/consultar-examen':
            resp = crudexamenes.consultar_examen()
            for fecha in resp:
                fecha['FechaRealizacion'] = str(fecha['FechaRealizacion'])
                fecha['FechaResultados'] = str(fecha['FechaResultados'])
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

        elif self.path == '/consultar-tratamiento':
            resp = crudtratamientos.consultar_tratamiento()
            for fecha in resp:
                fecha['FechaIniciar'] = str(fecha['FechaIniciar'])
                fecha['FechaFinalizar'] = str(fecha['FechaFinalizar'])
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

        elif self.path == '/permitir-entrada-paciente':
            print(paciente)
            print('SE CONSULTO POR PACIENTE')
            if paciente['id'] is None:
                resp = False
            else:
                resp = True
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

        elif self.path == '/permitir-entrada-personal':
            print(personal)
            print('SE CONSULTO POR PERSOL')
            if personal['id'] is None:
                resp = False
            else:
                resp = True
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))
            
        else:
            return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        global paciente
        global personal
        global token
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        data = data.decode('utf-8')
        data = parse.unquote(data)
        data = json.loads(data)

        if self.path == '/paciente':
            crear_y_login = False
            if data['accion'] == 'nuevo-login':
                crear_y_login = True
                data['accion'] = 'nuevo'
            resultado = crudpaciente.administrar_paciente(data)
            print(resultado)
            if data['accion'] == 'nuevo' or data['accion'] == 'modificar' and resultado == 'Registro procesado con exito':
                foto = data['foto']
                matriz = np.array([np.fromstring(foto, np.uint8, sep=',')])
                matriz = matriz.reshape(200, 200, 3)
                if data['accion'] == 'nuevo':
                    id = resultado[1]
                    resultado = resultado[0]
                else:
                    id = data['id']

                if crear_y_login:
                    paciente['dui'] = data['dui']
                    paciente['id'] = resultado[1]
                    paciente['nombre'] = data['nombre']

                inteligencia.guardar_rostro('icon/pacientes/', matriz, id)

        if self.path == '/personal':
            crear_y_login = False
            if data['accion'] == 'nuevo-login':
                crear_y_login = True
                data['accion'] = 'nuevo'
            resultado = crudpersonal.administrar_personal(data)
            print(resultado)
            if data['accion'] == 'nuevo' or data['accion'] == 'modificar' and resultado == 'Registro procesado con exito':
                foto = data['foto']
                matriz = np.array([np.fromstring(foto, np.uint8, sep=',')])
                matriz = matriz.reshape(200, 200, 3)
                if data['accion'] == 'nuevo':
                    id = resultado[1]
                    resultado = resultado[0]
                else:
                    id = data['id']

                if crear_y_login:
                    personal['dui'] = data['dui']
                    personal['id'] = resultado[1]
                    personal['nombre'] = data['nombre']

                inteligencia.guardar_rostro('icon/personal/', matriz, id)

        elif self.path == '/iniciar_sesion':
            resultado = crudpaciente.identificar(data['dui'])
            if resultado != False:
                id = int(resultado[0]['idPaciente'])
                foto = data['imagen']
                matriz = np.array([])
                matriz = np.fromstring(foto, np.uint8, sep=',')
                matriz = matriz.reshape(200, 200, 3)

                comparar = inteligencia.iniciar_sesion('icon/pacientes/', matriz, id)

                if comparar == True:
                    paciente['dui'] = resultado[0]['DUI']
                    paciente['id'] = resultado[0]['idPaciente']
                    paciente['nombre'] = resultado[0]['Nombre']
                    resultado = True
                else:
                    resultado = False
            else:
                resultado = False

        elif self.path == '/iniciar_sesion_personal':
            resultado = crudpersonal.identificar(data['dui'])
            print(resultado)
            if resultado != False:
                id = int(resultado[0]['idPersonal'])
                foto = data['imagen']
                matriz = np.array([])
                matriz = np.fromstring(foto, np.uint8, sep=',')
                matriz = matriz.reshape(200, 200, 3)

                comparar = inteligencia.iniciar_sesion('icon/personal/', matriz, id)

                if comparar == True:
                    print(personal)
                    personal['dui'] = resultado[0]['DUI']
                    personal['id'] = resultado[0]['idPersonal']
                    personal['nombre'] = resultado[0]['Nombre']
                    resultado = True
                else:
                    resultado = False
            else:
                resultado = False

        elif self.path == '/cerrar_sesion':
            print('CERRANDO SESION')
            paciente['id'] = None
            paciente['dui'] = None
            paciente['nombre'] = None
            resultado = True

        elif self.path == '/cerrar_sesion_personal':
            print('CERRANDO SESION')
            personal['id'] = None
            personal['dui'] = None
            personal['nombre'] = None
            resultado = True

        elif self.path == '/proveedor':
            resultado = crudproveedor.administrar_proveedor(data)

        elif self.path == '/medicamento':
            resultado = crudmedicamentos.administrar_medicamento(data)

        elif self.path == '/turno':
            resultado = crudturnos.administrar_turno(data)

        elif self.path == '/especialidad':
            resultado = crudespecialidades.administrar_especialidad(data)

        elif self.path == '/receta':
            resultado = crudrecetas.administrar_receta(data)

        elif self.path == '/admintir':
            resultado = crud.permitir_entrada(data)

        elif self.path == '/sintoma':
            resultado = crudsintoma.administrar_sintoma(data)

        elif self.path == '/enfermedad':
            resultado = crudenfermedades.administrar_enfermedad(data)

        elif self.path == '/cita':
            if data['accion'] == 'nuevo-usuario':
                data['idPaciente'] = paciente['id']
                data['accion'] = 'nuevo'
            resultado = crudcitas.administrar_citas(data)

        elif self.path == '/tipo-examen':
            resultado = crudtipoexamen.administrar_tipo_examen(data)

        elif self.path == '/tipo-tratamiento':
            resultado = crudtipotratamiento.administrar_tipo_tratamiento(data)

        elif self.path == '/examen':
            resultado = crudexamenes.administrar_examen(data)

        elif self.path == '/tratamiento':
            resultado = crudtratamientos.administrar_tratamiento(data)

        elif self.path == '/consultar-personal-turno':
            resultado = crudpersonal.consultar_personal_turno(data['idTurno'])

        elif self.path == '/dev':
            resultado = False
            if data['token'] == token:
                resultado = True
            else:
                resultado = False
            
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(dict(resultado=resultado)).encode('utf-8'))

print('Servidor iniciado en el puerto 3008')
servidor = HTTPServer(('localhost', 3008), servidorBasico)
servidor.serve_forever()