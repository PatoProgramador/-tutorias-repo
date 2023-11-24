from config.sql_conn import Conector
from tutores.tutores import Tutores
from Estudiantes.estudiantes import Estudiantes
from METODOS_DE_PAGO.METODOS_DE_PAGO import Metodos_pago

# Instancia de la conexion
sqlConn = Conector()
# inicio del cursor
sqlConn.dbConnect(hst="localhost", usr="root", pas="", dat="tutorias")

def menu():
    print("Lista de tablas disponibles: ")
    print("1. Tutores")
    print("2. Estudiantes")
    print("3. Metodos de pago")
    print("0. Salir")

# main
def main():
    contin = True
    while contin:
        menu()
        operation = int(input('Seleccione la tabla en la que desea realizar una operacion: '))
        # Crud tutores
        if operation == 1:
            tutores_crud = Tutores()
            aux = True
            while aux:
                tutores_crud.menu_tutores()
                tutor_op = int(input('Escriba la operacion que desea realizar con la tabla tutores: '))
                # Obtener todos los tutores
                if tutor_op == 1:
                    tutores_all = tutores_crud.get_all_stmt()
                    tutores = sqlConn.get_all(tutores_all)
                    print("----------------TUTORES-----------------")
                    for tutor in tutores:
                        print(tutor)
                    print("----------------------------------------")
                    res = input('¿Desea continuar realizando operaciones en tutores? S o N: ')
                    if res == 'N':
                        aux = False
                # Crear tutor
                if tutor_op == 2:
                    id = input('Ingrese el id: ')
                    nombres = input('Ingrese los nombres: ')
                    apellidos = input('Ingrese los apellidos: ')
                    pais = input('Ingrese el pais: ')
                    
                    data = (id, nombres, apellidos, pais)
                    tutor_create_stmt = tutores_crud.create_tutor_stmt()
                    
                    sqlConn.create_instance(tutor_create_stmt,data)
                    res = input('¿Desea continuar realizando operaciones en tutores? S o N: ')
                    if res == 'N':
                        aux = False
                if tutor_op == 5:
                    aux = False
        # Crud estudiantes
        if operation == 2:
            estudiantes_crud = Estudiantes()
            aux = True
            while aux:
                estudiantes_crud.menu_estudiantes()
                est_op = int(input('Escriba la operacion que desea realizar con la tabla estudiantes: '))
                # Obtener todos los estudiantes
                if est_op == 1:
                    estudiantes_all = estudiantes_crud.get_all_stmt()
                    estudiantes = sqlConn.get_all(estudiantes_all)
                    print("----------------ESTUDIANTES-----------------")
                    for est in estudiantes:
                        print(est)
                    print("----------------------------------------")
                    res = input('¿Desea continuar realizando operaciones en estudiantes? S o N: ')
                    if res == 'N':
                        aux = False
                # Crear estudiante
                if est_op == 2:
                    id = int(input('Ingrese el id: '))
                    nombres = input('Ingrese los nombres: ')
                    apellidos = input('Ingrese los apellidos: ')
                    
                    data = (id, nombres, apellidos)
                    estudiante_create_stmt = estudiantes_crud.create_estudiantes_stmt()
                    
                    sqlConn.create_instance(estudiante_create_stmt,data)
                    res = input('¿Desea continuar realizando operaciones en estudiantes? S o N: ')
                    if res == 'N':
                        aux = False


                if est_op == 5:
                    aux = False
        # Crud metodos de pago
        if operation == 3:
            metodos_pago_crud = Metodos_pago()
            aux = True
            while aux:
                metodos_pago_crud.menu_pagos()
                est_op = int(input('Escriba la operacion que desea realizar con la tabla de metodos de pago: '))
                # Obtener todos los metodos de pago
                if est_op == 1:
                    metodos_pago_all = metodos_pago_crud.get_all_stmt()
                    metodos_pago = sqlConn.get_all(metodos_pago_all)
                    print("----------------METODOS DE PAGO-----------------")
                    for metodo in metodos_pago:
                        print(metodo)
                    print("----------------------------------------")
                    res = input('¿Desea continuar realizando operaciones en metodos de pago? S o N: ')
                    if res == 'N':
                        aux = False
                # Crear metodo de pago
                if est_op == 2:
                    id = int(input('Ingrese el id: '))
                    nombres_metodo = input('Ingrese el nombre del metodo de pago: ')
                    tipo_metodo = input('Ingrese el tipo del metodo de pago: ')
                    
                    data = (id, nombres_metodo, tipo_metodo)
                    create_metodo_stmt = metodos_pago_crud.create_pagos_stmt()
                    
                    sqlConn.create_instance(create_metodo_stmt,data)
                    res = input('¿Desea continuar realizando operaciones en los metodos de pago? S o N: ')
                    if res == 'N':
                        aux = False


                if est_op == 5:
                    aux = False
                    
        if operation == 0:
            contin = False
            
main()
