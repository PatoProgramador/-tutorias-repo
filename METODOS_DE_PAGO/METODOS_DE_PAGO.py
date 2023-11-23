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
#     "INSERT INTO metodos_de_pago (ID_METODOS_DE_PAGO, NOMBRE_METODO_DE_PAGO, TIPO_METODO_DE_PAGO)"
#     "VALUES (%s, %s, %s)"
# )

# Datos
# id = int(input('Ingrese el ID: '))
# nombre= input('Ingrese el nombre de su metodo de pago: ')
# tipo = input('Ingrese el tipo de pago (tarjeta credito/debito,pse,biletera movil): ')

# data = (id, nombre, tipo)

 
# mycursor.execute(insert_stmt, data)
# mydb.commit()
# -----------------------------------READ--------------------------------------------------------------------
# Consulta para seleccionar todos los registros
# select_stmt = "SELECT * FROM metodos_de_pago"

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
#     "UPDATE metodos_de_pago SET NOMBRE_METODO_DE_PAGO=%s, TIPO_METODO_DE_PAGO=%s WHERE ID_METODO_DE_PAGO=%s"
# )

# # Ejecutar la sentencia de actualización
# mycursor.execute(update_stmt, nuevos_datos)

# # Hacer commit para aplicar los cambios
# mydb.commit()
# ----------------------------------------DELETE--------------------------------------------------------------
# # ID del tutor a eliminar
# id = int(input('Ingrese el id a borrar: '))

# # Sentencia de eliminación
# delete_stmt = "DELETE FROM metodos_de_pago WHERE ID_METODOS_DE_PAGO = %s"

# # Ejecutar la sentencia de eliminación
# mycursor.execute(delete_stmt, (id))

# # Hacer commit para aplicar los cambios
# mydb.commit()
