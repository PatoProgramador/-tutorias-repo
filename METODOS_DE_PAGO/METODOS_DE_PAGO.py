class Metodos_pago:
    
    def menu_pagos(self):
        print("Lista de operaciones disponibles: ")
        print("1) Obtener todos los metodos de pago")
        print("2) Crear un metodo de pago")
        print("3) Actualizar los datos de un metodo de pago")
        print("4) Eliminar un metodo de pago")
        print("5) Salir de las operaciones de metodos de pago")

    def get_all_stmt(self):
        select_stmt = "SELECT * FROM (metodos_de_pago)"
        
        return select_stmt

    def create_pagos_stmt(self):
        insert_stmt = (
            "INSERT INTO (metodos_de_pago) (ID_METODOS_DE_PAGO, NOMBRE_METODO_DE_PAGO, TIPO_METODO_DE_PAGO)"
            "VALUES (%s, %s, %s)"
        )
        
        return insert_stmt
    
    def update_pagos_stmt(self):
        update_stmt = (
            "UPDATE metodos_de_pago SET NOMBRE_METODO_DE_PAGO=%s, TIPO_METODO_DE_PAGO=%s WHERE ID_METODO_DE_PAGO=%s"
        )
        
        return update_stmt
    
    def update_pagos_stmt(self):
        delete_stmt = "DELETE FROM metodos_de_pago WHERE ID_METODOS_DE_PAGO = %s"
        
        return delete_stmt
