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
                # 7) TUTORIAS
                if ad_Op == 3:
                    print('---------------------------------------------------------')
                    id_estudiante = input('Ingrese el numero de documento del aprendiz: ')
                    id_tutor = input('Digite el numero de documento del tutor: ')
                    id_area_conocimiento = input('Ingrese el Id del area de conocimiento: ')
                    fecha_tutoria = input('Ingrese la fecha la cual fue efectuada la tutoria(en formato YYYY-MM-DD): ')
                    tiempo_tutoria = int(input('Ingrese el tiempo que duro la tutoria: '))
                    calificacion_tutor = int(input('Ingrese la calificacion del tutor: '))
                    calificacion_estudiante = int(input('Ingrese la calificacion del estudiante: '))
                    valor_tutoria = input('Ingrese el valor que tuvo la tutoria: ')
                    
                    data = (id_estudiante, id_tutor, id_area_conocimiento, fecha_tutoria, tiempo_tutoria, calificacion_tutor, calificacion_estudiante, valor_tutoria)
                    create_tutoria_stmt = adminUser.create_tutoria()
                    
                    sqlConn.create_instance(create_tutoria_stmt, data)
                    print('---------------------------------------------------------')
                    print('|               tutoria creada correctamente             |')
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
                    print('---------------------------------------------------------')
                    id_tutor = input('Digite su numero de documento: ')
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
                    print('---------------------------------------------------------')
                    id_tutor = input('Ingrese su numero de documento: ')
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
                    print('-----------------------------------------------------------------------')
                    print('|        Tu servicio se ha registrado correctamente en el area         |')
                    print('-----------------------------------------------------------------------')
                if tutorOp == 0:
                    aux = False
        # estudiantes
        if opt == 3:
            estudianteUser = Estudiantes()
            aux = True
            while aux:
                estudianteUser.menu_estudiantes()
                estOp = int(input('Escriba la operacion que desea realizar: '))
                # 5) APRENDICES
                if estOp == 1:
                    print('---------------------------------------------------------')
                    id_estudiante = input('Ingrese su numero de documento: ')
                    nombres_estudiante = input('Ingrese sus nombres: ')
                    apellidos_estudiante = input('Ingrese sus apellidos: ')
                    email_estudiante = input('Ingrese su correo electronico: ')
                    # mostrar paises
                    print('----Lista de paises disponibles----')
                    paises_get_stmt = instance_Catalog.get_all_paises_stmt()
                    paises = sqlConn.get_all(paises_get_stmt)
                    for pais in paises:
                        print(pais)
                    
                    pais_estudiante = input('Digite el código de tres digitos de alguno de los paises disponibles: ')
                    
                    data = (id_estudiante, nombres_estudiante, apellidos_estudiante, email_estudiante, pais_estudiante)
                    create_estudiante_stmt = estudianteUser.create_estudiantes_stmt()
                    
                    sqlConn.create_instance(create_estudiante_stmt, data)
                    print('---------------------------------------------------------')
                    print('|     Te haz registrado como aprendiz correctamente      |')
                    print('---------------------------------------------------------')
                # 6) AGENDA_TUTORES_APRENDICES
                if estOp == 2:
                    print('---------------------------------------------------------')
                    id_estudiante = input('Ingrese su numero de documento: ')
                    print('----Lista de areas de conocimiento disponibles----')
                    areas_get_stmt = instance_Catalog.get_all_areas_conocimiento()
                    areas_conocimiento = sqlConn.get_all(areas_get_stmt)
                    for area in areas_conocimiento:
                        print(area)
                    id_area_conocimiento = input('Digite la abreviatura del area de conocimiento de su interes: ')
                    # Consulta con filtro por area de conocimiento
                    print('----Lista de tutores y sus tarifas disponibles para esta area (el primer valor es su cedula y el segundo es la tarifa)----')
                    tutor_areas_stmt = instance_Catalog.get_all_tutores_areas()
                    tutores_areas = sqlConn.get_all_sorted(tutor_areas_stmt, (id_area_conocimiento,))
                    for tutor_area in tutores_areas:
                        print(tutor_area)

                    id_tutor = input('Digite la cedula del tutor de su interes: ')
                    fecha = input('Ingrese la fecha en la que desea agendar(en formato YYYY-MM-DD): ')
                    tiempo = int(input('Ingrese el tiempo que considera se tardará la tutoria: '))
                    
                    data = (id_tutor, fecha, id_estudiante, tiempo, id_area_conocimiento)
                    estudiante_agenda_stmt = estudianteUser.create_estudiante_agenda_stmt()
                    
                    sqlConn.create_instance(estudiante_agenda_stmt, data)
                    print('---------------------------------------------------------')
                    print('|       Tu tutoria ha sido agendada correctamente        |')
                    print('---------------------------------------------------------')
                if estOp == 0:
                    aux = False
        if opt == 0:
            contin = False
main()