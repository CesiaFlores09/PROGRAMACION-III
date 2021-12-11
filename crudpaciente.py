import conexionbd

bd = conexionbd.conectar()

class curdpacientes:
    def consultar_paciente(self):
        sql = "SELECT * FROM pacientes"
        usuario = bd.consultar(sql)
        for Fecha in usuario:
            Fecha['FechaNacimiento'] = Fecha['FechaNacimiento'].strftime("%d/%m/%Y")
        return usuario

    def consultar_a_paciente(self, id):
        sql = f"SELECT * FROM pacientes WHERE idPaciente={id}"
        usuario = bd.consultar(sql)
        for Fecha in usuario:
            Fecha['FechaNacimiento'] = Fecha['FechaNacimiento'].strftime("%d/%m/%Y")
        sql = f"SELECT citas.idConsulta, citas.idPaciente, citas.idPersonal, citas.FechaCita, citas.Detalles, GROUP_CONCAT(sintomas.Nombre) AS sintomas, pacientes.Nombre AS paciente, personal.Nombre AS personal FROM citas INNER JOIN detalle_cita ON citas.idConsulta=detalle_cita.idCita INNER JOIN sintomas ON detalle_cita.idSintoma=sintomas.idSintoma INNER JOIN pacientes ON citas.idPaciente=pacientes.idPaciente INNER JOIN personal ON citas.idPersonal=personal.idPersonal GROUP BY citas.idConsulta HAVING citas.idPaciente={id} ORDER BY citas.FechaCita DESC"
        citas = bd.consultar(sql)
        for Fecha in citas:
            Fecha['FechaCita'] = Fecha['FechaCita'].strftime("%d/%m/%Y")
        sql = f"SELECT e.idExamen, e.idTipoExamen, t.Nombre AS tipoExamen, e.idCita, e.FechaRealizacion, e.FechaResultados, e.Estado, GROUP_CONCAT(d.idEnfermedad) AS enfermedades, GROUP_CONCAT(en.Nombre) AS nombreEnfermedades, GROUP_CONCAT(e.Estado) AS estadoEnfermedades, p.Nombre FROM examenes e INNER JOIN detalle_examenes d ON e.idExamen=d.idExamen INNER JOIN enfermedades en ON d.idEnfermedad=en.idEnfermedad INNER JOIN citas c ON e.idCita=c.idConsulta INNER JOIN pacientes p ON c.idPaciente=p.idPaciente INNER JOIN tipo_examen t ON e.idTipoExamen=t.idTipo WHERE p.idPaciente={id} GROUP BY e.idExamen ORDER BY e.FechaRealizacion DESC"
        examenes = bd.consultar(sql)
        for Fecha in examenes:
            Fecha['FechaRealizacion'] = Fecha['FechaRealizacion'].strftime("%d/%m/%Y")
            Fecha['FechaResultados'] = Fecha['FechaResultados'].strftime("%d/%m/%Y")
        sql = f"SELECT t.idTratamiento, t.idTipo, e.idTipoExamen, e.idExamen, te.Nombre AS nombreExamen, tt.Nombre AS nombreTratamiento, t.FechaIniciar, t.FechaFinalizar, t.Estado, p.Nombre FROM tratamientos t INNER JOIN tipo_tratamiento tt ON t.idTipo = tt.idTratamiento INNER JOIN detalle_tratamientos dt ON t.idTratamiento=dt.idTratamiento INNER JOIN examenes e ON dt.idExamen=e.idExamen INNER JOIN tipo_examen te ON e.idTipoExamen = te.idTipo LEFT JOIN citas c ON e.idCita = c.idConsulta LEFT JOIN pacientes p ON c.idPaciente = p.idPaciente WHERE p.idPaciente = {id} GROUP BY t.idTratamiento ORDER BY t.FechaIniciar DESC"
        tratamientos = bd.consultar(sql)
        for Fecha in tratamientos:
            Fecha['FechaIniciar'] = Fecha['FechaIniciar'].strftime("%d/%m/%Y")
            Fecha['FechaFinalizar'] = Fecha['FechaFinalizar'].strftime("%d/%m/%Y")
        return usuario, citas, examenes, tratamientos

    def identificar(self, data):
        sql = f"SELECT * FROM pacientes WHERE DUI='{data}'"
        resultado = bd.consultar(sql)
        for Fecha in resultado:
            Fecha['FechaNacimiento'] = Fecha['FechaNacimiento'].strftime("%d/%m/%Y")
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