class Tutores:
    
    def menu_tutores(self):
        print("Lista de operaciones disponibles: ")
        print("1) Obtener todos los tutores")
        print("2) Crear un tutor")
        print("3) Actualizar los datos de un tutor")
        print("4) Eliminar un tutor")
        print("5) Salir de las operaciones de tutores")

    def get_all_stmt(self):
        select_stmt = "SELECT * FROM awdawd"
        
        return select_stmt

    def create_tutor_stmt(self):
        insert_stmt = (
            "INSERT INTO tutores (ID_TUTORES, NOMBRES_TUTORES, APELLIDOS_TUTORES, PAIS_TUTOR)"
            "VALUES (%s, %s, %s, %s)"
        )
        
        return insert_stmt
