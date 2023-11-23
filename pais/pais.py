import mysql.connector

# Conection
mydb = mysql.connector.connect(
    host ="localhost", user="root", password="", database="tutorias"
)
# Ejecuciones en la db
mycursor = mydb.cursor()
# CRUD- CREATE, READ, UPDATE, DELETE
# ------------------------------CREAR INSTANCIAS-----------CTRL+K + CTRL+C--------------------------------------------------------------CTRL+K CTRL+U
# insert_stmt = (
#     "INSERT INTO pais(ID_PAIS,  ACRO, NOMBRE_PAIS)"
#     "VALUES (%s, %s, %s)"
# )

# # Datos
# id = int(input('Ingrese el ID: '))
# acro = input('Ingrese el acronimo: ')
# nombre = input('Ingrese el nombre: ')

# data = (id, acro, nombre)

 
# mycursor.execute(insert_stmt, data)
# mydb.commit()
# -----------------------------------READ--------------------------------------------------------------------
# Consulta para seleccionar todos los registros
# select_stmt = "SELECT * FROM pais"

# # Ejecutar la consulta
# mycursor.execute(select_stmt)

# # Obtener todos los resultados
# resultados = mycursor.fetchall()

# # Mostrar los resultados
# for resultado in resultados:
#     print(resultado)
# ---------------------------------------UPDATE----------------------------------------------------------------
# #Datos para la actualización
# id = int(input('Ingrese el id a modificar: '))

# nuevos_datos = ("testdeUpdate", "test", id)


# # Sentencia de actualización
# update_stmt = (
#     "UPDATE pais SET ACRO=%s, NOMBRE_PAIS=%s WHERE ID_PAIS=%s"
# )

# # Ejecutar la sentencia de actualización
# mycursor.execute(update_stmt, nuevos_datos)

# # Hacer commit para aplicar los cambios
# mydb.commit()
# ----------------------------------------DELETE--------------------------------------------------------------
# ID del tutor a eliminar
id = int(input('Ingrese el id a borrar: '))

# Sentencia de eliminación
delete_stmt = "DELETE FROM pais WHERE ID_PAIS = %s"

# Ejecutar la sentencia de eliminación
mycursor.execute(delete_stmt, id)

# Hacer commit para aplicar los cambios
mydb.commit()
