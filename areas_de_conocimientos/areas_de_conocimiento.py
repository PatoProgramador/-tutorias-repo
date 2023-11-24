class Areas_conocimiento:
    
    def menu_estudiantes(self):
        print("Lista de operaciones disponibles: ")
        print("1) Ingrese la cantidad de áreas de conocimiento de su interés")
        print("2) Digite el nombre de sus areas de interés")
        print("3) Salir de las operaciones de áreas de conocimiento")

    def get_all_stmt(self):
        select_stmt = "SELECT * FROM (areas_conocimiento))"
        
        return select_stmt

    def create_estudiantes_stmt(self):
        insert_stmt = (
            "INSERT INTO (areas_conocimiento) (ID_AREA_CONOCIMIENTO, CANTIDAD_AREAS, NOMBRE_AREAS)"
            "VALUES (%s, %s, %s)"
        )
        
        return insert_stmt
    
    def update_estudiantes_stmt(self):
        update_stmt = (
            "UPDATE areas_conocimiento SET CANTIDAD_AREAS=%s, NOMBRE_AREAS=%s WHERE ID_AREA_CONOCIMIENTO=%s"
        )
        
        return update_stmt
    
    def update_tutor_stmt(self):
        delete_stmt = "DELETE FROM metodos_de_pago WHERE ID_AREA_CONOCIMIENTO = %s"
        
        return delete_stmt