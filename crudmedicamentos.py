import conexionbd

bd = conexionbd.conectar()

class curdmedicamento:
    def consultar_medicamento(self):
        sql = "SELECT * FROM medicamentos"
        return bd.consultar(sql)

    def administrar_medicamento(self, data):
        try:
            if data["accion"]=="nuevo":
                sql = "INSERT INTO medicamentos (idMedicamento, idProveedor, Nombre, Precio, Cantidad) VALUES(%s, %s, %s, %s, %s)"
                id = bd.auto_increment('medicamento')
                val = (id, data["idProveedor"], data["nombre"], data["precio"], data["cantidad"])

            elif data["accion"]=="modificar":
                sql = "UPDATE medicamentos SET idProveedor=%s, Nombre=%s, Precio=%s, Cantidad=%s WHERE idMedicamento=%s"
                val = (data["idProveedor"], data["nombre"], data["precio"], data["cantidad"], data["id"])

            elif data["accion"]=="eliminar":
                sql = "DELETE FROM medicamentos WHERE idMedicamento=%s"
                val = (data["id"],)

            return bd.ejecutar_consulta(sql, val)
        except Exception as e:
            return str(e)