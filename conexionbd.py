import mysql.connector

class conectar:
    def __init__(self):
        self.conexion = mysql.connector.connect(host="localhost", user="root",
                                            passwd="admin123", database="clinica")

        if self.conexion.is_connected():
            print("Conectado")
        else:
            print("Error al conectar")

    def consultar(self, sql):
        try:
            cursor = self.conexion.cursor(dictionary=True)
            cursor.execute(sql)
            resultado = cursor.fetchall()
            return resultado
        except Exception as e:
            print(e)
            return False

    def ejecutar_consulta(self, sql, val):
        try:
            print(sql, val)
            cursor = self.conexion.cursor()
            cursor.execute(sql, val)
            self.conexion.commit()
            return "Registro procesado con exito"
        except Exception as e:
            print(e)
            return False

    def auto_increment(self, tabla):
        try:
            if tabla == 'pacientes':
                sql = 'SELECT MAX(idPaciente) AS id FROM pacientes'
            elif tabla == 'personal':
                sql = 'SELECT MAX(idPersonal) AS id FROM personal'
            elif tabla == 'proveedor':
                sql = 'SELECT MAX(idProveedor) AS id FROM proveedores'
            elif tabla == 'medicamento':
                sql = 'SELECT MAX(idMedicamento) AS id FROM medicamentos'
            elif tabla == 'recetas':
                sql = 'SELECT MAX(idReceta) AS id FROM recetas'
            elif tabla == 'turnos':
                sql = 'SELECT MAX(idTurno) AS id FROM turnos'
            elif tabla == 'especialidad':
                sql = 'SELECT MAX(idEspecialidad) AS id FROM especialidad'
            resultado = self.consultar(sql)
            if resultado[0]['id'] is None:
                return 0
            else:
                return resultado[0]['id']+1
        except Exception as e:
            print(e)
            return False