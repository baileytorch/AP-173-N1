from data.asignaturas import asignaturas
from data.crear_data import crear_data
from data.conexion import ejecutar_consulta
from prettytable import PrettyTable

# READ
def mostrar_listado_asignaturas():
    print()
    print('Listado de Asignaturas')
    listado_asignaturas = ejecutar_consulta('SELECT id_asignatura,codigo_asig,nombre_asig FROM asignaturas')
    tabla_asignaturas = PrettyTable()
    tabla_asignaturas.field_names = ['Id','Código Asignatura','Nombre Asignatura']
    for asignatura in listado_asignaturas:
        tabla_asignaturas.add_row(asignatura) # type: ignore
    print(tabla_asignaturas)

# READ
def buscar_asignatura():
    busqueda = input('Ingrese asignatura a buscar: ')
    for asignatura in asignaturas:
        if busqueda.lower() in asignatura.lower():
            return asignatura

def indice_asignatura(busqueda):
    for i in range(len(asignaturas)):
        if busqueda.lower() in asignaturas[i].lower():
            return i

# # CREATE
# def agregar_asignatura():
#     mostrar_listado_asignaturas()
#     nueva_asignatura = input('Ingrese nueva asignatura: ')
#     asignaturas.append(nueva_asignatura.title())

#     crear_data('asignaturas.py','asignaturas',asignaturas)

#     mostrar_listado_asignaturas()

# # UPDATE  
# def actualizar_asignatura():
#     mostrar_listado_asignaturas()
#     busqueda = input('Ingrese asignatura a buscar: ')
#     indice = indice_asignatura(busqueda)
#     # nuevo_dato = input(f'Ingrese nuevo nombre para asignatura {asignaturas[indice]}: ')
#     # asignaturas[indice] = nuevo_dato

#     crear_data('asignaturas.py','asignaturas',asignaturas)
#     mostrar_listado_asignaturas()

mostrar_listado_asignaturas()