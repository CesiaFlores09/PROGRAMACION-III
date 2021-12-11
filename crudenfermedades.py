import conexionbd

bd = conexionbd.conectar()

class curdenfermedad:
    def consultar_enfermedad(self):
        sql = "SELECT e.idEnfermedad, e.Nombre, e.Detalles, GROUP_CONCAT(s.Nombre SEPARATOR ',') as sintomas, GROUP_CONCAT(s.idSintoma SEPARATOR ',') as idsintomas FROM enfermedades e LEFT JOIN sintoma_enfermedad se ON e.idEnfermedad = se.idEnfermedad LEFT JOIN sintomas s ON se.idSintoma = s.idSintoma GROUP BY e.idEnfermedad"
        return bd.consultar(sql)

    def administrar_enfermedad(self, data):
        try:
            if data["accion"]=="nuevo":
                sql = "INSERT INTO enfermedades (idEnfermedad, Nombre, Detalles) VALUES (%s, %s, %s)"
                id = bd.auto_increment('enfermedad')
                val = (id, data["nombre"], data["detalles"])
                bd.ejecutar_consulta(sql, val)
                print(data['sintomas'])
                for sintoma in data["sintomas"]:
                    print(sintoma)
                    sql = "INSERT INTO sintoma_enfermedad (idEnfermedad, idSintoma) VALUES (%s, %s)"
                    val = (id, sintoma)
                    bd.ejecutar_consulta(sql, val)

            elif data["accion"]=="modificar":
                sql = "DELETE FROM sintoma_enfermedad WHERE idEnfermedad = %s"
                val = (data["id"],)
                bd.ejecutar_consulta(sql, val)
                sql = "UPDATE enfermedades SET Nombre = %s, Detalles = %s WHERE idEnfermedad = %s"
                val = (data["nombre"], data["detalles"], data["id"])
                bd.ejecutar_consulta(sql, val)
                for sintoma in data["sintomas"]:
                    sql = "INSERT INTO sintoma_enfermedad (idEnfermedad, idSintoma) VALUES (%s, %s)"
                    val = (data["id"], sintoma)
                    bd.ejecutar_consulta(sql, val)

            elif data["accion"]=="eliminar":
                sql = "DELETE FROM sintoma_enfermedad WHERE idEnfermedad = %s"
                val = (data["id"],)
                bd.ejecutar_consulta(sql, val)
                sql = "DELETE FROM enfermedades WHERE idEnfermedad = %s"
                val = (data["id"],)
                bd.ejecutar_consulta(sql, val)

            return "Registro procesado con exito"
        except Exception as e:
            return str(e)