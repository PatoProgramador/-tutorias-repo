class Estudiantes:
    
    def menu_estudiantes(self):
        print("Lista de operaciones disponibles: ")
        print("1) Obtener todos los estudiantes")
        print("2) Crear un estudiante")
        print("3) Actualizar los datos de un estudiante")
        print("4) Eliminar un estudiante")
        print("5) Salir de las operaciones de estudiantes")

    def get_all_stmt(self):
        select_stmt = "SELECT * FROM (ESTUDIANTES)"
        
        return select_stmt

    def create_estudiantes_stmt(self):
        insert_stmt = (
            "INSERT INTO (ESTUDIANTES) (ID_ESTUDIANTE, NOMBRE_ESTUDIANTE, APELLIDOS_ESTUDIANTE)"
            "VALUES (%s, %s, %s)"
        )
        
        return insert_stmt
    
    def update_estudiantes_stmt(self):
        update_stmt = (
            "UPDATE ESTUDIANTES SET NOMBRE_ESTUDIANTE=%s, APELLIDOS_ESTUDIANTE=%s WHERE ID_ESTUDIANTE=%s"
        )
        
        return update_stmt
    
    def update_estudiantes_stmt(self):
        delete_stmt = "DELETE FROM ESTUDIANTES WHERE ID_ESTUDIANTE = %s"
        
        return delete_stmt