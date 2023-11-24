class Paises:
    
    def menu_estudiantes(self):
        print("Lista de operaciones disponibles: ")
        print("1) Obtener todos los paises")
        print("2) Crear un pais")
        print("3) Actualizar los datos de un pais")
        print("4) Eliminar un pais")
        print("5) Salir de las operaciones de paises")

    def get_all_stmt(self):
        select_stmt = "SELECT * FROM (PAISES)"
        
        return select_stmt

    def create_pais_stmt(self):
        insert_stmt = (
            "INSERT INTO (PAISES) (ID_PAIS, NOMBRE_PAIS)"
            "VALUES (%s, %s)"
        )
        
        return insert_stmt
    
    def update_pais_stmt(self):
        update_stmt = (
            "UPDATE PAISES SET NOMBRE_PAIS=%s WHERE ID_PAIS=%s"
        )
        
        return update_stmt
    
    def update_pais_stmt(self):
        delete_stmt = "DELETE FROM PAISES WHERE ID_PAIS = %s"
        
        return delete_stmt