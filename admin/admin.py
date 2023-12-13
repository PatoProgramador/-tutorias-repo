class Admin:
    
    def admin_menu(self):
        print("Lista de operaciones disponibles: ")
        print("1. Crear pais")
        print("2. Crear area de conocimiento")

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