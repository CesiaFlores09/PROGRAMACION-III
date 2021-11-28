import conexionbd

bd = conexionbd.conectar()

class curdproveedor:
    def consultar_proveedor(self):
        sql = "SELECT * FROM proveedores"
        return bd.consultar(sql)

    def administrar_proveedor(self, data):
        try:
            if data["accion"]=="nuevo":
                sql = "INSERT INTO proveedores (idProveedor, Nombre, Telefono, Direccion) VALUES(%s, %s, %s, %s)"
                id = bd.auto_increment('proveedor')
                val = (id, data["nombre"], data["telefono"], data["direccion"],)

            elif data["accion"]=="modificar":
                sql = "UPDATE proveedores SET Nombre=%s, Telefono=%s, Direccion=%s WHERE idProveedor=%s"
                val = (data["nombre"], data["telefono"], data["direccion"], data["id"])

            elif data["accion"]=="eliminar":
                sql = "DELETE FROM proveedores WHERE idProveedor=%s"
                val = (data["id"],)

            return bd.ejecutar_consulta(sql, val)
        except Exception as e:
            return str(e)