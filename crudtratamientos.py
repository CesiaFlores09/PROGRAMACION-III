import conexionbd

bd = conexionbd.conectar()

class curdtratamiento:
    def consultar_tratamiento(self):
        sql = "SELECT t.idTratamiento, t.idTipo, e.idTipoExamen, e.idExamen, te.Nombre AS nombreExamen, tt.Nombre AS nombreTratamiento, t.FechaIniciar, t.FechaFinalizar, t.Estado, p.Nombre FROM tratamientos t INNER JOIN tipo_tratamiento tt ON t.idTipo = tt.idTratamiento INNER JOIN detalle_tratamientos dt ON t.idTratamiento=dt.idTratamiento INNER JOIN examenes e ON dt.idExamen=e.idExamen INNER JOIN tipo_examen te ON e.idTipoExamen = te.idTipo LEFT JOIN citas c ON e.idCita = c.idConsulta LEFT JOIN pacientes p ON c.idPaciente = p.idPaciente"
        return bd.consultar(sql)

    def administrar_tratamiento(self, data):
        try:
            if data["accion"]=="nuevo":
                sql = "INSERT INTO tratamientos (idTratamiento, idTipo, FechaIniciar, FechaFinalizar, Estado) VALUES (%s, %s, %s, %s, %s)"
                id = bd.auto_increment("tratamiento")
                valores = (id, data["idTipo"], data["fechaInicio"], data["fechaFinal"], data["estado"])
                bd.ejecutar_consulta(sql, valores)
                sql = "INSERT INTO detalle_tratamientos (idTratamiento, idExamen) VALUES (%s, %s)"
                valores = (id, data["idExamen"])
                bd.ejecutar_consulta(sql, valores)

            elif data["accion"]=="modificar":
                sql = "UPDATE tratamientos SET idTipo=%s, FechaIniciar=%s, FechaFinalizar=%s, Estado=%s WHERE idTratamiento=%s"
                valores = (data["idTipo"], data["fechaInicio"], data["fechaFinal"], data["estado"], data["idTratamiento"])
                bd.ejecutar_consulta(sql, valores)
                sql = "UPDATE detalle_tratamientos SET idExamen=%s WHERE idTratamiento=%s"
                valores = (data["idExamen"], data["idTratamiento"])
                bd.ejecutar_consulta(sql, valores)

            elif data["accion"]=="eliminar":
                sql = "DELETE FROM detalle_tratamientos WHERE idTratamiento=%s"
                valores = (data["idTratamiento"],)
                bd.ejecutar_consulta(sql, valores)
                sql = "DELETE FROM tratamientos WHERE idTratamiento=%s"
                valores = (data["idTratamiento"],)
                bd.ejecutar_consulta(sql, valores)

            return "Registro procesado con exito"
        except Exception as e:
            return str(e)