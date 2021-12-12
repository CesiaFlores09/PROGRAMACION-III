import conexionbd

bd = conexionbd.conectar()

class curdtipo_examen:
    def consultar_tipo_examen(self):
        sql = "SELECT * FROM tipo_examen"
        return bd.consultar(sql)

    def administrar_tipo_examen(self, data):
        try:
            print(data)
            if data["accion"]=="nuevo":
                sql = "INSERT INTO tipo_examen (idTipo, Nombre, Detalles) VALUES (%s, %s, %s)"
                id = bd.auto_increment("tipo_examen")
                valores = (id, data["nombre"], data["detalles"])

            elif data["accion"]=="modificar":
                sql = "UPDATE tipo_examen SET Nombre=%s , Detalles=%s WHERE idTipo=%s"
                valores = (data["nombre"], data["detalles"], data["id"])

            elif data["accion"]=="eliminar":
                sql = "DELETE FROM tipo_examen WHERE idTipo=%s"
                valores = (data["id"],)

            return bd.ejecutar_consulta(sql, valores)
        except Exception as e:
            return str(e)