class Estudiantes:
    
    def menu_estudiantes(self):
        print("Lista de operaciones disponibles: ")
        print("1) Obtener todos los paises")
        print("2) Crear un pais")
        print("3) Actualizar los datos de un tutor")
        print("4) Eliminar un tutor")
        print("5) Salir de las operaciones de tutores")

    def get_all_stmt(self):
        select_stmt = "SELECT * FROM (nombre de la tabla)"
        
        return select_stmt

    def create_estudiantes_stmt(self):
        insert_stmt = (
            "INSERT INTO (nombre de tabla) (ID_TUTORES, NOMBRES_TUTORES, APELLIDOS_TUTORES, PAIS_TUTOR)"
            "VALUES (%s, %s, %s, %s)"
        )
        
        return insert_stmt
    
    def update_estudiantes_stmt(self):
        update_stmt = (
            "UPDATE metodos_de_pago SET NOMBRE_METODO_DE_PAGO=%s, TIPO_METODO_DE_PAGO=%s WHERE ID_METODO_DE_PAGO=%s"
        )
        
        return update_stmt
    
    def update_tutor_stmt(self):
        delete_stmt = "DELETE FROM metodos_de_pago WHERE ID_METODOS_DE_PAGO = %s"
        
        return delete_stmt