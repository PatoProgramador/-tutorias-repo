import mysql.connector

# Conection
mydb = mysql.connector.connect(
    host ="localhost", user="root", password="", database="tutorias"
)
# Operation
insert_stmt = (
    "INSERT INTO tutores(ID_TUTORES,  NOMBRES_TUTORES, APELLIDOS_TUTORES,  PAIS_TUTOR)"
    "VALUES (%s, %s, %s, %s)"
)

# Datos
id = int(input('Ingrese el ID: '))
nombres = input('Ingrese el Nombre: ')
apellidos = input('Ingrese el Apellido: ')
pais = input('Ingrese el Pais: ')

data = (id, nombres, apellidos, pais)
 
# Ejecuciones en la db
mycursor = mydb.cursor()
 
mycursor.execute(insert_stmt, data)

mydb.commit()

# update
# select *
# delete
