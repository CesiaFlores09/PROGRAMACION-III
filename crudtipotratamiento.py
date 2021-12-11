import conexionbd

bd = conexionbd.conectar()

class curdtipo_tratamiento:
    def consultar_tipo_tratamiento(self):
        sql = "SELECT * FROM tipo_tratamiento"
        return bd.consultar(sql)

    def administrar_tipo_tratamiento(self, data):
        try:
            if data["accion"]=="nuevo":
                sql = "INSERT INTO tipo_tratamiento (idTratamiento, Nombre, Detalles) VALUES (%s, %s, %s)"
                id = bd.auto_increment("tipo_tratamiento")
                valores = (id, data["nombre"], data["detalles"])

            elif data["accion"]=="modificar":
                sql = "UPDATE tipo_tratamiento SET Nombre=%s , Detalles=%s WHERE idTratamiento=%s"
                valores = (data["nombre"], data["detalles"], data["id"])

            elif data["accion"]=="eliminar":
                sql = "DELETE FROM tipo_tratamiento WHERE idTratamiento=%s"
                valores = (data["id"],)

            return bd.ejecutar_consulta(sql, valores)
        except Exception as e:
            return str(e)