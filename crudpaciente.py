import conexionbd

bd = conexionbd.conectar()

class curdpacientes:
    def consultar_paciente(self):
        sql = "SELECT * FROM pacientes"
        usuario = bd.consultar(sql)
        for Fecha in usuario:
            Fecha['FechaNacimiento'] = Fecha['FechaNacimiento'].strftime("%d/%m/%Y")
        return usuario

    def identificar(self, data):
        sql = f"SELECT idPaciente FROM pacientes WHERE DUI='{data}'"
        resultado = bd.consultar(sql)
        if len(resultado) == 1:
            return resultado
        else:
            return False

    def administrar_paciente(self, data):
        try:
            if data["accion"]=="nuevo":
                sql = "INSERT INTO pacientes (idPaciente, DUI, NIT, Nombre, Sexo, Telefono, Correo, Direccion, FechaNacimiento, Foto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                id = bd.auto_increment('pacientes')
                val = (id, data["dui"], data["nit"], data["nombre"], data["sexo"], data["telefono"], data["correo"], data["direccion"], data["fechaNacimiento"], 'icon/pacientes/perfil'+str(id)+'.jpg')

            elif data["accion"]=="modificar":
                sql = "UPDATE pacientes SET DUI=%s, NIT=%s, Nombre=%s, Sexo=%s, Telefono=%s, Correo=%s, Direccion=%s, FechaNacimiento=%s, Foto=%s WHERE idPaciente=%s"
                val = (data["dui"], data["nit"], data["nombre"], data["sexo"], data["telefono"], data["correo"], data["direccion"], data["fechaNacimiento"], 'icon/pacientes/perfil'+str(data["id"])+'.jpg', data["id"])

            elif data["accion"]=="eliminar":
                sql = "DELETE FROM pacientes WHERE idPaciente=%s"
                val = (data["id"],)

            if data["accion"] == "nuevo":
                return bd.ejecutar_consulta(sql, val), id
            else:
                return bd.ejecutar_consulta(sql, val)
        except Exception as e:
            return str(e)