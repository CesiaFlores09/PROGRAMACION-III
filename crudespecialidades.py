import conexionbd

bd = conexionbd.conectar()

class curdespecialidad:
    def consultar_especialidad(self):
        sql = "SELECT * FROM especialidad"
        return bd.consultar(sql)

    def administrar_especialidad(self, data):
        try:
            print(data)
            if data["accion"]=="nuevo":
                sql = "INSERT INTO especialidad (idEspecialidad, Nombre) VALUES (%s, %s)"
                id = bd.auto_increment("especialidad")
                valores = (id, data["nombre"])

            elif data["accion"]=="modificar":
                sql = "UPDATE especialidad SET Nombre=%s WHERE idEspecialidad=%s"
                valores = (data["nombre"], data["id"])

            elif data["accion"]=="eliminar":
                sql = "DELETE FROM especialidad WHERE idEspecialidad=%s"
                valores = (data["id"],)

            return bd.ejecutar_consulta(sql, valores)
        except Exception as e:
            return str(e)