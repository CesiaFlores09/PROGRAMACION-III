import conexionbd

bd = conexionbd.conectar()

class curdcitas:
    def consultar_citas(self):
        sql = "SELECT citas.idConsulta, citas.idPaciente, citas.idPersonal, citas.FechaCita, citas.Detalles, GROUP_CONCAT(sintomas.Nombre) AS sintomas, pacientes.Nombre AS paciente, personal.Nombre AS personal FROM citas INNER JOIN detalle_cita ON citas.idConsulta=detalle_cita.idCita INNER JOIN sintomas ON detalle_cita.idSintoma=sintomas.idSintoma INNER JOIN pacientes ON citas.idPaciente=pacientes.idPaciente INNER JOIN personal ON citas.idPersonal=personal.idPersonal GROUP BY citas.idConsulta"
        usuario = bd.consultar(sql)
        for fecha in usuario:
            fecha["FechaCita"] = fecha["FechaCita"].strftime("%d/%m/%Y %H:%M")
        return usuario

    def administrar_citas(self, data):
        try:
            if data["accion"]=="nuevo":
                sql = "INSERT INTO citas (idConsulta, idPaciente, idPersonal, FechaCita, Detalles) VALUES (%s, %s, %s, %s, %s)"
                id = bd.auto_increment("cita")
                val = (id, data["idPaciente"], data["idPersonal"], data["fecha"], data["detalles"])
                bd.ejecutar_consulta(sql, val)
                for sintoma in data["sintomas"]:
                    sql = "INSERT INTO detalle_cita (idCita, idSintoma) VALUES (%s, %s)"
                    val = (id, sintoma)
                    bd.ejecutar_consulta(sql, val)

            elif data["accion"]=="modificar":
                sql = "UPDATE citas SET idPaciente=%s, idPersonal=%s, FechaCita=%s, Detalles=%s WHERE idConsulta=%s"
                val = (data["idPaciente"], data["idPersonal"], data["fecha"], data["detalles"], data["idConsulta"])
                bd.ejecutar_consulta(sql, val)
                sql = "DELETE FROM detalle_cita WHERE idCita=%s"
                val = (data["id"],)
                bd.ejecutar_consulta(sql, val)
                for sin in data["sintomas"]:
                    sql = "INSERT INTO detalle_cita (idCita, idSintoma) VALUES (%s, %s)"
                    val = (data["idConsulta"], sin)
                    bd.ejecutar_consulta(sql, val)

            elif data["accion"]=="eliminar":
                sql = "DELETE FROM detalle_cita WHERE idCita=%s"
                val = (data["id"],)
                bd.ejecutar_consulta(sql, val)
                sql = "DELETE FROM citas WHERE idConsulta=%s"
                val = (data["id"],)
                bd.ejecutar_consulta(sql, val)

            return "Registro procesado con exito"
        except Exception as e:
            return str(e)