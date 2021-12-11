import conexionbd

bd = conexionbd.conectar()

class curdexamen:
    def consultar_examen(self):
        sql = "SELECT e.idExamen, e.idTipoExamen, t.Nombre AS tipoExamen, e.idCita, e.FechaRealizacion, e.FechaResultados, e.Estado, GROUP_CONCAT(d.idEnfermedad) AS enfermedades, GROUP_CONCAT(en.Nombre) AS nombreEnfermedades, GROUP_CONCAT(e.Estado) AS estadoEnfermedades, p.Nombre FROM examenes e INNER JOIN detalle_examenes d ON e.idExamen=d.idExamen INNER JOIN enfermedades en ON d.idEnfermedad=en.idEnfermedad INNER JOIN citas c ON e.idCita=c.idConsulta INNER JOIN pacientes p ON c.idPaciente=p.idPaciente INNER JOIN tipo_examen t ON e.idTipoExamen=t.idTipo GROUP BY e.idExamen"
        return bd.consultar(sql)

    def administrar_examen(self, data):
        try:
            if data["accion"]=="nuevo":
                sql = "INSERT INTO examenes (idExamen, idTipoExamen, idCita, FechaRealizacion, FechaResultados, Estado) VALUES (%s, %s, %s, %s, %s, %s)"
                id = bd.auto_increment("examen")
                valores = (id, data["idTipoExamen"], data["idCita"], data["fechaRealizacion"], data["fechaResultados"], data["estado"])
                bd.ejecutar_consulta(sql, valores)
                for enfermedad in data["enfermedades"]:
                    sql = "INSERT INTO detalle_examenes (idExamen, idEnfermedad, Estado) VALUES (%s, %s, %s)"
                    valores = (id, enfermedad, data["estado"])
                    bd.ejecutar_consulta(sql, valores)

            elif data["accion"]=="modificar":
                sql = "UPDATE examenes SET FechaResultados=%s, Estado=%s WHERE idExamen=%s AND Estado NOT LIKE '2'"
                valores = (data["fechaResultados"], data["estado"], data["idExamen"])
                bd.ejecutar_consulta(sql, valores)
                bd.ejecutar_consulta(sql, valores)
                for enfermedad in data["enfermedades"]:
                    sql = "UPDATE detalle_examenes SET Estado=%s WHERE idExamen=%s AND idEnfermedad=%s AND Estado NOT LIKE '2'"
                    valores = (data["estado"], data["idExamen"], enfermedad)
                    bd.ejecutar_consulta(sql, valores)

            elif data["accion"]=="eliminar":
                sql = "DELETE FROM detalle_examenes WHERE idExamen=%s"
                valores = (data["id"],)
                bd.ejecutar_consulta(sql, valores)
                sql = "DELETE FROM examenes WHERE idExamen=%s"
                valores = (data["id"],)
                bd.ejecutar_consulta(sql, valores)

            return "Registro procesado con exito"
        except Exception as e:
            return str(e)