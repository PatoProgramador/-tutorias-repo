class Catalogos:
    
    def get_all_paises_stmt(self):
        insert_stmt = (
            "SELECT * FROM paises"
        )
        
        return insert_stmt
    
    def get_all_areas_conocimiento(self):
        insert_stmt = (
            "SELECT * FROM areas_conocimiento"
        )
        
        return insert_stmt
    
    def get_all_tutores_areas(self):
        insert_stmt = (
            "SELECT ID_TUTOR, TARIFA FROM tutores_areas_conocimiento WHERE ID_AREA_CONOCIMIENTO = %s"
        )
        
        return insert_stmt