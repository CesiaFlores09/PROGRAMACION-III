import conexionbd

bd = conexionbd.conectar()

class curdturno:
    def consultar_turno(self):
        sql = "SELECT * FROM turnos"
        return bd.consultar(sql)

    def administrar_turno(self, data):
        try:
            print(data)
            if data["accion"]=="nuevo":
                sql = "INSERT INTO turnos (idTurno, Nombre, HoraInicio, HoraSalida, DiaInicio, DiaSalida) VALUES (%s, %s, %s, %s, %s, %s)"
                id = bd.auto_increment("turnos")
                valores = (id, data["nombre"], data["horaInicio"], data["horaSalida"], data["diaInicio"], data["diaSalida"])

            elif data["accion"]=="modificar":
                sql = "UPDATE turnos SET Nombre=%s, HoraInicio=%s, HoraSalida=%s, DiaInicio=%s, DiaSalida=%s WHERE idTurno=%s"
                valores = (data["nombre"], data["horaInicio"], data["horaSalida"], data["diaInicio"], data["diaSalida"], data["id"])

            elif data["accion"]=="eliminar":
                sql = "DELETE FROM turnos WHERE idTurno=%s"
                valores = (data["id"],)

            return bd.ejecutar_consulta(sql, valores)
        except Exception as e:
            return str(e)