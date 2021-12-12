import conexionbd

bd = conexionbd.conectar()

class curdsintoma:
    def consultar_sintoma(self):
        sql = "SELECT * FROM sintomas"
        return bd.consultar(sql)

    def administrar_sintoma(self, data):
        try:
            if data["accion"]=="nuevo":
                sql = "INSERT INTO sintomas (idSintoma, Nombre, Detalles) VALUES (%s, %s, %s)"
                id = bd.auto_increment('sintoma')
                val = (id, data["nombre"], data["detalles"])

            elif data["accion"]=="modificar":
                sql = "UPDATE sintomas SET Nombre=%s, Detalles=%s WHERE idSintoma=%s"
                val = (data["nombre"], data["detalles"], data["id"])

            elif data["accion"]=="eliminar":
                sql = "DELETE FROM sintomas WHERE idSintoma=%s"
                val = (data["id"],)

            return bd.ejecutar_consulta(sql, val)
        except Exception as e:
            return str(e)