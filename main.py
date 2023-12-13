from config.sql_conn import Conector
from admin.admin import Admin
from tutores.tutores import Tutores
from Estudiantes.estudiantes import Estudiantes
from METODOS_DE_PAGO.METODOS_DE_PAGO import Metodos_pago

# Instancia de la conexion
sqlConn = Conector()
# inicio del cursor
sqlConn.dbConnect(hst="localhost", usr="root", pas="", dat="tutorias")

def menu():
    print('--Roles--')
    print("1. Admin")
    print("2. Estudiante")
    print("3. Tutor")
    print("0. Salir")

# main
def main():
    contin = True
    while contin:
        menu()
        opt = int(input('Seleccione su rol: '))
        # Admin
        if opt == 1:
            # Instancia de la clase
            adminUser = Admin()
            aux = True
            while aux:
                adminUser.admin_menu()
                ad_Op = int(input('Escriba la operacion que desea realizar: '))
                # Paises
                if ad_Op == 1:
                    print('---------------------------------------------------------')
                    id_pais = input('Ingrese el código de tres digitos del pais: ')
                    # manejo de error
                    while len(id_pais) != 3:
                        id_pais = input('El codigo debe ser solamente de tres digitos, ingrese uno valido, por favor: ')
        
                    nombre_pais = input('Ingrese el nombre del pais: ')
                    # operaciones en la db
                    data = (id_pais, nombre_pais)
                    create_pais_stmt = adminUser.create_pais_stmt()
                    
                    sqlConn.create_instance(create_pais_stmt, data)
                    print('---------------------------------------------------------')
                    print('|               Pais creado correctamente                |')
                    print('---------------------------------------------------------')
                # Areas de conocimiento
                if ad_Op == 2:
                    print('---------------------------------------------------------')
                    id_area_conocimiento = input('Ingrese el Id del area de conocimiento: ')
                    nombre_area_conocimiento = input('Ingrese el nombre del area de conocimiento: ')
                    
                    data = (id_area_conocimiento, nombre_area_conocimiento)
                    create_area_conocimiento_stmt = adminUser.create_area_conocimiento()
                    
                    sqlConn.create_instance(create_area_conocimiento_stmt, data)
                    print('---------------------------------------------------------')
                    print('|        Area de conocimiento creada correctamente       |')
                    print('---------------------------------------------------------')
                if ad_Op == 0:
                    aux = False                    
                    
main()