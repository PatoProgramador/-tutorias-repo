class Admin:
    
    def admin_menu(self):
        print("Lista de operaciones disponibles: ")
        print("1. Crear pais")
        print("2. Crear area de conocimiento")
        print("3. Crear una tutoria")
        print("0. Regresar al menu principal")

    def create_pais_stmt(self):
        insert_stmt = (
            "INSERT INTO paises (ID_PAIS, NOMBRE_PAIS)"
            "VALUES (%s, %s)"
        )
        
        return insert_stmt
    
    def create_area_conocimiento(self):
        insert_stmt = (
            "INSERT INTO areas_conocimiento (ID_AREA_CONOCIMIENTO, NOMBRE_AREA_CONOCIMIENTO)"
            "VALUES (%s, %s)"
        )
        
        return insert_stmt
    
    def create_tutoria(self):
        insert_stmt = (
            "INSERT INTO tutorias (ID_APRENDIZ_TUTORIA, ID_TUTOR_TUTORIA, ID_AREA_CONOCIMIENTO_TUTORIA, FECHA_TUTORIA, TIEMPO_TUTORIA, CALIFICACION_TUTOR,  CALIFICACION_ESTUDIANTE, VALOR_TUTORIA)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        )
        
        return insert_stmt