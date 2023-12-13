class Estudiantes:
    
    def menu_estudiantes(self):
        print("Lista de operaciones disponibles: ")
        print("1. Registrarse en la app")
        print("2. Agendar una tutoria")
        print("0. Regresar al menu principal")

    def create_estudiantes_stmt(self):
        insert_stmt = (
            "INSERT INTO aprendices (CEDULA_APRENDICES, NOMBRES_APRENDICES, APELLIDOS_APRENDICES, CORREO_ELECTRONICO_APRENDICES, PÁIS_APRENDICES)"
            "VALUES (%s, %s, %s, %s, %s)"
        )
        
        return insert_stmt
    
    def create_estudiante_agenda_stmt(self):
        insert_stmt = (
            "INSERT INTO agenda_tutores_aprendices (ID_TUTOR, FECHA, ID_APRENDIZ, TIEMPO, ID_AREA_CONOCIMIENTO)"
            "VALUES (%s, %s, %s, %s, %s)"
        )
        
        return insert_stmt
