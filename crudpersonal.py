import conexionbd

bd = conexionbd.conectar()

class curdpersonal:
    def consultar_personal(self):
        # Seleccionar todo de la tabla personal y de la tabla turnos_personal conseguir todos los turnos para cada personal
        sql = "SELECT personal.idPersonal, personal.DUI, personal.NIT, personal.Nombre, personal.Sexo, personal.Telefono, personal.Correo, personal.Direccion, personal.FechaNacimiento, personal.Foto, personal.idEspecialidad, especialidad.Nombre AS Especialidad, GROUP_CONCAT(turnos.idTurno) AS idTurnos, GROUP_CONCAT(turnos.Nombre) AS Turnos FROM personal LEFT JOIN turnos_personal ON personal.idPersonal=turnos_personal.idPersonal LEFT JOIN turnos ON turnos_personal.idTurno=turnos.idTurno LEFT JOIN especialidad ON personal.idEspecialidad=especialidad.idEspecialidad GROUP BY personal.idPersonal"
        usuario = bd.consultar(sql)
        for Fecha in usuario:
            Fecha['FechaNacimiento'] = Fecha['FechaNacimiento'].strftime("%d/%m/%Y")
        return usuario

    def administrar_personal(self, data):
        try:
            if data["accion"]=="nuevo":
                sql = "INSERT INTO personal (idPersonal, DUI, NIT, Nombre, Sexo, Telefono, Correo, Direccion, FechaNacimiento, Foto, idEspecialidad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                id = bd.auto_increment('personal')
                val = (id, data["dui"], data["nit"], data["nombre"], data["sexo"], data["telefono"], data["correo"], data["direccion"], data["fechaNacimiento"], 'icon/personal/perfil'+str(id)+'.jpg', data["idEspecialidad"])
                bd.ejecutar_consulta(sql, val)
                for turno in data["turnos"]:
                    sql = "INSERT INTO turnos_personal (idTurno, idPersonal) VALUES (%s, %s)"
                    val = (turno, id)
                    bd.ejecutar_consulta(sql, val)

            elif data["accion"]=="modificar":
                sql = "UPDATE personal SET DUI=%s, NIT=%s, Nombre=%s, Sexo=%s, Telefono=%s, Correo=%s, Direccion=%s, FechaNacimiento=%s, Foto=%s, idEspecialidad=%s WHERE idPersonal=%s"
                val = (data["dui"], data["nit"], data["nombre"], data["sexo"], data["telefono"], data["correo"], data["direccion"], data["fechaNacimiento"], 'icon/personal/perfil'+str(data["id"])+'.jpg', data["idEspecialidad"], data["id"])
                bd.ejecutar_consulta(sql, val)
                sql = "DELETE FROM turnos_personal WHERE idPersonal=%s"
                val = (data["id"],)
                bd.ejecutar_consulta(sql, val)
                for turno in data["turnos"]:
                    sql = "INSERT INTO turnos_personal (idTurno, idPersonal) VALUES (%s, %s)"
                    val = (turno, data["id"])
                    bd.ejecutar_consulta(sql, val)

            elif data["accion"]=="eliminar":
                sql = "DELETE FROM personal WHERE idPersonal=%s"
                val = (data["id"],)
                bd.ejecutar_consulta(sql, val)
                sql = "DELETE FROM turnos_personal WHERE idPersonal=%s"
                val = (data["id"],)
                bd.ejecutar_consulta(sql, val)

            if data["accion"] == "nuevo":
                return "Registro procesado con exito", id
            else:
                return "Registro procesado con exito"
        except Exception as e:
            return str(e)