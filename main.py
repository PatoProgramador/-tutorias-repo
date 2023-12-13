from config.sql_conn import Conector
from catalogs.catalogs import Catalogos
from admin.admin import Admin
from tutores.tutores import Tutores
from Estudiantes.estudiantes import Estudiantes

# Instancia de la conexion
sqlConn = Conector()
# inicio del cursor
sqlConn.dbConnect(hst="localhost", usr="root", pas="", dat="tutorias")

def menu():
    print('--Roles--')
    print("1. Admin")
    print("2. Tutor")
    print("3. Estudiante")
    print("0. Salir")

# main
def main():
    contin = True
    while contin:
        instance_Catalog = Catalogos()
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
                # 1) PAISES
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
                # 2) AREAS DE CONOCIMIENTO
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
        # Tutor (operaciones)
        if opt == 2:
            tutorUser = Tutores()
            aux = True
            while aux:
                tutorUser.menu_tutores()
                tutorOp = int(input('Escriba la operacion que desea realizar: '))
                # 3) TUTORES (crear en tabla)
                if tutorOp == 1:
                    id_tutor = input('Digite su numero de cedula: ')
                    nombres_tutor = input('Digite sus nombres: ')
                    apellidos_tutor = input('Digite sus apellidos: ')
                    email_tutor = input('Digite su correo electronico: ')
                    # mostrar paises
                    print('----Lista de paises disponibles----')
                    paises_get_stmt = instance_Catalog.get_all_paises_stmt()
                    paises = sqlConn.get_all(paises_get_stmt)
                    for pais in paises:
                        print(pais)
                        
                    pais_tutor = input('Digite el código de tres digitos de alguno de los paises disponibles: ')
                    
                    data = (id_tutor, nombres_tutor, apellidos_tutor, email_tutor, pais_tutor)
                    create_tutor_stmt = tutorUser.create_tutor_stmt()
                    
                    sqlConn.create_instance(create_tutor_stmt, data)
                    print('---------------------------------------------------------')
                    print('|       Te haz registrado como tutor correctamente       |')
                    print('---------------------------------------------------------')
                # 4) TUTORES_AREAS_CONOCIMIENTO
                if tutorOp == 2:
                    id_tutor = input('Ingrese su numero de cedula')
                    # mostrar areas de conocimiento
                    print('----Lista de areas de conocimiento disponibles----')
                    areas_get_stmt = instance_Catalog.get_all_areas_conocimiento()
                    areas_conocimiento = sqlConn.get_all(areas_get_stmt)
                    for area in areas_conocimiento:
                        print(area)
                    
                    id_area_conocimiento = input('Ingrese la abreviatura del area de conocimiento en la que desea ofertar su servicio: ')
                    tarifa = int(input('Ingrese su tarifa: '))
                    
                    data = (id_tutor, id_area_conocimiento, tarifa)
                    create_tutor_area_stmt = tutorUser.create_tutor_area_conocimiento_stmt()
                    sqlConn.create_instance(create_tutor_area_stmt, data)
                    print('---------------------------------------------------------')
                    print('|        Tu servicio se ha registrado en el area         |')
                    print('---------------------------------------------------------')
                                    
main()