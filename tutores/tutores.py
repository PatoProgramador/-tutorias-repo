class Tutores:
    
    def menu_tutores(self):
        print("Lista de operaciones disponibles: ")
        print("1. Registrarse en la app")
        print("2. Ofrecer servicio en un area de conocimiento")
        print("0. Regresar al menu principal")

    def create_tutor_stmt(self):
        insert_stmt = (
            "INSERT INTO tutores (ID_TUTORES, NOMBRES_TUTORES, APELLIDOS_TUTORES, CORREO_ELECTRONICO_TUTORES, PAIS_TUTOR)"
            "VALUES (%s, %s, %s, %s, %s)"
        )
        
        return insert_stmt
    
    def create_tutor_area_conocimiento_stmt(self):
        insert_stmt = (
            "INSERT INTO tutores_areas_conocimiento (ID_TUTOR, ID_AREA_CONOCIMIENTO, TARIFA)"
            "VALUES (%s, %s, %s)"
        )
        
        return insert_stmt