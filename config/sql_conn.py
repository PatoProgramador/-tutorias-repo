import mysql.connector

class Conector:
    
    #Metodos
    def dbConnect(self, hst,usr, pas, dat):
        try:
            self.cursor = mysql.connector.connect(
                host=hst, user=usr, password=pas, database=dat
            )
            print('Conexión con la base de datos exitosa')
        except mysql.connector.Error as e:
            # Manejo de excepciones específicas de MySQL
            print(f"Error de MySQL: {e}")

    def get_all(self, stmt:str):
        cursor = self.cursor.cursor()
        
        cursor.execute(stmt)
        
        resultados = cursor.fetchall()
        
        return resultados
    
    def create_instance(self, stmt:str, data):
        cursor = self.cursor.cursor()
        
        cursor.execute(stmt, data)
        
        last_insert_id = cursor.lastrowid
        print(f"Instancia creada con ID: {last_insert_id}")
        
        self.cursor.commit()
        
        
# # Conection
# mydb = mysql.connector.connect(
#     host ="localhost", user="root", password="", database="tutorias"
# )
# # Ejecuciones en la db
# mycursor = mydb.cursor()