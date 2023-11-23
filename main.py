from config.sql_conn import Conector
from tutores.tutores import Tutores

# Instancia de la conexion
sqlConn = Conector()
# inicio del cursor
sqlConn.dbConnect(hst="localhost", usr="root", pas="", dat="tutorias")

def menu():
    print("Lista de tablas disponibles: ")
    print("1. Tutores")
    print("2. Pais")
    print("3. Estudiantes")
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
                    
        if operation == 0:
            contin = False
            
main()
