import conexionbd

bd = conexionbd.conectar()

class curdreceta:
    def consultar_receta(self):
        sql = "SELECT r.idReceta, r.idPaciente, r.idPersonal, r.Detalles, p.Nombre, p.Apellido, m.Nombre, m.Precio, m.Cantidad FROM recetas r INNER JOIN detalle_recetas d ON r.idReceta=d.idReceta INNER JOIN medicamentos m ON d.idMedicamento=m.idMedicamento INNER JOIN pacientes p ON r.idPaciente=p.idPaciente"
        sql = "SELECT recetas.idReceta, recetas.idPaciente, recetas.idPersonal, recetas.Detalles, medicamentos.idMedicamento, medicamentos.Nombre FROM recetas INNER JOIN detalle_recetas ON recetas.idReceta=detalle_recetas.idReceta INNER JOIN medicamentos ON detalle_recetas.idMedicamento=medicamentos.idMedicamento"
        sql = "SELECT * FROM recetas"
        return bd.consultar(sql)

    def administrar_receta(self, data):
        try:
            if data["accion"]=="nuevo":
                sql = "INSERT INTO recetas (idReceta, idPaciente, idPersonal, Detalles) VALUES (%s, %s, %s, %s)"
                id = bd.auto_increment("recetas")
                valores = (id, data["idPaciente"], data["idPersonal"], data["Detalles"])
                bd.ejecutar_consulta(sql, valores)
                for medicamento in data["medicamentos"]:
                    sql = "INSERT INTO detalle_recetas (idReceta, idMedicamento) VALUES (%s, %s)"
                    valores = (id, medicamento)
                    bd.ejecutar_consulta(sql, valores)

            elif data["accion"]=="modificar":
                sql = "UPDATE medicamentos SET idProveedor=%s, Nombre=%s, Precio=%s, Cantidad=%s WHERE idMedicamento=%s"
                valores = (data["idProveedor"], data["Nombre"], data["Precio"], data["Cantidad"], data["idMedicamento"])
                bd.ejecutar_consulta(sql, valores)
                sql = "DELETE FROM detalle_recetas WHERE idReceta=%s"
                valores = (data["id"],)
                bd.ejecutar_consulta(sql, valores)
                for medicamento in data["medicamentos"]:
                    sql = "INSERT INTO detalle_recetas (idReceta, idMedicamento) VALUES (%s, %s)"
                    valores = (data["id"], medicamento)

            elif data["accion"]=="eliminar":
                sql = "DELETE FROM detalle_recetas WHERE idMedicamento=%s"
                valores = (data["idMedicamento"],)
                bd.ejecutar_consulta(sql, valores)
                sql = "DELETE FROM medicamentos WHERE idMedicamento=%s"
                valores = (data["idMedicamento"],)
                bd.ejecutar_consulta(sql, valores)

            return "Registro procesado con exito"
        except Exception as e:
            return str(e)