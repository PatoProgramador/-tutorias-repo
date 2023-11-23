import mysql.connector

class SqlConnector:
    # Constructor
    def __init__(self, hst: str, us: str, pas: str, db: str):
        self.host = hst
        self.user = us
        self.password = pas
        self.database = db

    # Método
    def connector(self):
        mydb = mysql.connector.connect(
                host=self.host, user=self.user, password=self.password, database=self.database
            )
        print("Conexión exitosa a la base de datos.")
        return mydb