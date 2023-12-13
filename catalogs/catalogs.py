class Catalogos:
    
    def get_all_paises_stmt(self):
        insert_stmt = (
            "SELECT * FROM paises"
        )
        
        return insert_stmt
    
    def get_all_areas_conocimiento(self):
        insert_stmt = (
            "SELECT * areas_conocimiento"
        )
        
        return insert_stmt