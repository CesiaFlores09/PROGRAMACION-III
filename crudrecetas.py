import conexionbd

bd = conexionbd.conectar()

class curdreceta:
    def consultar_receta(self):
        sql = "SELECT recetas.idReceta, recetas.idPaciente, recetas.idPersonal, recetas.Detalles, GROUP_CONCAT(detalle_recetas.idMedicamento) AS idMedicamentos, GROUP_CONCAT(medicamentos.Nombre) AS NombreMedicamentos FROM recetas INNER JOIN detalle_recetas ON recetas.idReceta=detalle_recetas.idReceta INNER JOIN medicamentos ON detalle_recetas.idMedicamento=medicamentos.idMedicamento GROUP BY recetas.idReceta"
        return bd.consultar(sql)

    def administrar_receta(self, data):
        try:
            if data["accion"]=="nuevo":
                sql = "INSERT INTO recetas (idReceta, idPaciente, idPersonal, Detalles) VALUES (%s, %s, %s, %s)"
                id = bd.auto_increment("recetas")
                valores = (id, data["idPaciente"], data["idPersonal"], data["detalles"])
                bd.ejecutar_consulta(sql, valores)
                for medicamento in data["medicamentos"]:
                    sql = "INSERT INTO detalle_recetas (idReceta, idMedicamento) VALUES (%s, %s)"
                    valores = (id, medicamento)
                    bd.ejecutar_consulta(sql, valores)

            elif data["accion"]=="modificar":
                sql = "UPDATE recetas SET idPaciente=%s, idPersonal=%s, Detalles=%s WHERE idReceta=%s"
                valores = (data["idPaciente"], data["idPersonal"], data["detalles"], data["id"])
                bd.ejecutar_consulta(sql, valores)
                print(data["medicamentos"], data["id"])
                sql = "DELETE FROM detalle_recetas WHERE idReceta=%s"
                valores = (data["id"],)
                bd.ejecutar_consulta(sql, valores)
                for medicamento in data["medicamentos"]:
                    sql = "INSERT INTO detalle_recetas (idReceta, idMedicamento) VALUES (%s, %s)"
                    valores = (data["id"], medicamento)
                    bd.ejecutar_consulta(sql, valores)

            elif data["accion"]=="eliminar":
                sql = "DELETE FROM detalle_recetas WHERE idReceta=%s"
                valores = (data["id"],)
                bd.ejecutar_consulta(sql, valores)
                sql = "DELETE FROM recetas WHERE idReceta=%s"
                valores = (data["id"],)
                bd.ejecutar_consulta(sql, valores)

            return "Registro procesado con exito"
        except Exception as e:
            return str(e)